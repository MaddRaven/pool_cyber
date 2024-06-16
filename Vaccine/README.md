# Cybersecurity Piscine Vaccine

## Overview

The Cybersecurity Piscine Vaccine is a Python-based tool designed to perform SQL injection tests on given URLs. It aims to educate users about SQL injection vulnerabilities and how to identify them. This tool is intended for legal testing purposes only and should not be used to exploit unauthorized websites.

## Features

- Performs SQL injection tests on provided URLs.
- Detects various types of SQL injection vulnerabilities including Union, Error, Boolean, Time, and Blind injections.
- Identifies the type of database engine to tailor tests for success.
- Extracts valuable information from vulnerable websites such as vulnerable parameters, payloads, database names, table names, column names, and complete database dumps.
- Supports both GET and POST methods for requests.
- Stores results in a file, creating it if it doesn't exist upon the first run.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. The project requires Python 3.x.

### Installation

To install the Cybersecurity Piscine Vaccine, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install required dependencies using pip.

## Usage

To use the Cybersecurity Piscine Vaccine, run the following command:
    - `./vaccine [-X method] [-o file] URL