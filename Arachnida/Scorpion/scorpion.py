#!/usr/bin/env python3

import sys
import exifread
from PIL import Image

def get_exif_data(image_path):
    print(f"Reading EXIF metadata of {image_path}")
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f)
            print(tags)
            return tags
    except IOError as e:
        print(f"Error during the reading of {image_path}: {e}")
        return {}

def display_metadata(tags):
    print("EXIF Metadata:")
    for tag in tags.keys():
        if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
            print(f"{tag}: {tags[tag]}")

def display_date_of_creation(tags):
    creation_date_tag = 'DateTimeOriginal'
    if creation_date_tag in tags:
        print(f"Date de création: {tags[creation_date_tag]}")
    else:
        print("Aucune date de création trouvée.")

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
            display_date_of_creation(tags)
        except IOError:
            print(f"Image {image_path} can't be opened")


if __name__ == "__main__":
    main()