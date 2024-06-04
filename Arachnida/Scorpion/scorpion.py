#!/usr/bin/env python3

import sys
from PIL import Image


def get_exif_data(image_path):
    print(f"Reading EXIF metadata of {image_path}")
    try:
            img = Image.open(image_path)
            exif_data = img._getexif()
            return exif_data
    except IOError as e:
        print(f"Error during the reading of {image_path}: {e}")
        return {}


def main():
    if len(sys.argv) < 2:
        print("Wrong number of arguments")
        sys.exit(1)

    with open('./scorpion.txt', 'r') as fichier:
        contenu = fichier.read()
        print(contenu)

    for image_path in sys.argv[1:]:
        try:
            image = Image.open(image_path)
            print(f"\nImage: {image_path}")
            tags = get_exif_data(image_path)
            print("EXIF metadata:")
        except IOError:
            print(f"Image {image_path} can't be opened")


if __name__ == "__main__":
    main()