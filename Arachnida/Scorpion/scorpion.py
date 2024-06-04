#!/usr/bin/env python3

import sys
from PIL import Image

def get_exif_data(image_path):
    print(f"Reading EXIF metadata of {image_path}")
    try:
        img = Image.open(image_path)
        if hasattr(img, '_getexif'):
            exif_data = img._getexif()
            if exif_data is not None:
                return exif_data
        else:
            print(f"The image format {image_path} does not support EXIF data.")
            return None
    except IOError as e:
        print(f"Error during the reading of {image_path}: {e}")
        return None


def print_exif(data):
    print(data)

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
            print(f"\n===\nImage: {image_path}")
            data = get_exif_data(image_path)
            print("EXIF metadata:")
            print_exif(data)
            print("===")
        except IOError:
            print(f"Image {image_path} can't be opened")


if __name__ == "__main__":
    main()