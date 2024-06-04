#!/usr/bin/env python3

import sys
from PIL import Image, ExifTags

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


def get_creation_date(exif_data):
    if exif_data is not None:
        for tag_id in exif_data.keys():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            if tag == 'DateTimeOriginal':
                print(f"Creation date : {exif_data[tag_id]}")
                break
        else:
            print("No creation date found")


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
            get_creation_date(data)
            print("EXIF metadata:")
            print_exif(data)
            print("===")
        except IOError:
            print(f"\nImage {image_path} can't be opened")


if __name__ == "__main__":
    main()