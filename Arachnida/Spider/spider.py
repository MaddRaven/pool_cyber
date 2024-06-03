#!/usr/bin/env python3

import os, argparse, requests, re
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def get_imgs(url):
    response = requests.get(url)
    imgs_url = []

    soup = BeautifulSoup(response.text, "lxml")
    imgs = soup.find_all('img')

    for img in imgs:
        img_url = img.attrs.get('src')
        if not img_url.startswith('http'):
            img_url = urljoin(url, img_url)
        imgs_url.append(img_url)
    
    return imgs_url


def download_imgs(imgs_url, path):
    if not os.path.exists(path):
        os.makedirs(path)

    for i, url in enumerate(imgs_url):
        try:
            response = requests.get(url)

            extension = url.split('.')[-1].lower()
            if (extension in ['jpg', 'jpeg', 'png', 'gif', 'bmp']):
                filename = f"{path}/image_{i}.{extension}"
                with open(filename, 'wb') as file:
                    file.write(response.content)
                print(f"Download OK: {filename}")
            else:
                print(f"Download KO: {path}/image_{i}:{extension}")

        except Exception as e:
            print(f"Error while downloading {url}: {str(e)}")


def create_web(url, path, level_max, depth):
    if depth > level_max:
        return

    response = requests.get(url)
    if response.status_code == 200:
        imgs_url = get_imgs(url)
        download_imgs(imgs_url, path)
    
        soup = BeautifulSoup(response.text, "lxml")
        for url in soup.find_all('a', href=True):
            url_link = url['href']
            if not url_link.startswith(('http:', 'https:')):
                url_link = urljoin(url, url_link)
            create_web(url_link, "{path}/{depth}_{i}", level_max, depth + 1)
    

def parse_arguments():
    parser = argparse.ArgumentParser("Spider program to download images")
    parser.add_argument('-r', '--recursive', action="store_true", help="Recursive Download")
    parser.add_argument('-l', '--level', type=int, default=5, help="Depth level of the recursive download")
    parser.add_argument('-p', '--path', default='./data/', help="Path of downloaded files")
    parser.add_argument('URL', help="URL targeted")
    return parser.parse_args()


def main():
    args = parse_arguments()
    url = args.URL
    path = args.path
    level_max = args.level

    if args.recursive:
        create_web(url, path, level_max, 0)
    else:
        response = requests.get(url)
        if response.status_code == 200:
            imgs_url = get_imgs(url)
            download_imgs(imgs_url, path)


if __name__ == "__main__":
    main()