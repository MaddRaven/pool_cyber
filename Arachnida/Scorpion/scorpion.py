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


def set_exif_data(image_path, save_path, exif_file_path="exif_data.txt"):
    print(f"Setting EXIF metadata of {image_path} based on {exif_file_path}")
    try:
        img = Image.open(image_path)
        if hasattr(img, '_getexif'):
            exif_data = img._getexif()

            with open(exif_file_path, 'r') as exif_file:
                lines = exif_file.readlines()

            new_exif_data = get_exif_data(image_path)


            if new_exif_data is None:
                new_exif_data = {}

            for line in lines:
                key_value = line.strip().split(':')
                if len(key_value) == 2:
                    key, value = key_value
                    new_exif_data[int(key)] = value

            if exif_data == None:
                exif_data = {}
                
            exif_data = dict(exif_data)
            exif_data.update(new_exif_data)

            img.save(save_path, exif=exif_data)
            print("Metadata successfully modified.")
        else:
            print("The image format does not support EXIF data.")
    except IOError as e:
        print(f"Error during the modification of {image_path}: {e}")


def delete_exif_data(image_path, save_path=None):
    print(f"Deleting EXIF metadata of {image_path}")
    try:
        img = Image.open(image_path)
        if hasattr(img, '_getexif'):
            img.info.pop('Exif', None)
            if save_path:
                img.save(save_path)
            else:
                img.save(image_path)
            print("EXIF metadata deleted.")
        else:
            print("The image format does not support EXIF data.")
    except IOError as e:
        print(f"Error during the deletion of {image_path}: {e}")


def print_data(data):
    for tag_id, value in data.items():
        tag = ExifTags.TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")


def main():
    if len(sys.argv) < 2:
        print("Wrong number of arguments")
        sys.exit(1)

    with open('./scorpion.txt', 'r') as fichier:
        contenu = fichier.read()
        print(contenu)

    action = None
    for i, arg in enumerate(sys.argv):
        if arg.startswith('-m') or arg.startswith('--modify'):
            action = 'modify'
            if i + 1 < len(sys.argv):
                target_image = sys.argv[i + 1]
                set_exif_data(target_image, 'modified_image.jpg', 'exif_data.txt')
                break
        elif arg.startswith('-d') or arg.startswith('--delete'):
            action = 'delete'
            if i + 1 < len(sys.argv):
                target_image = sys.argv[i + 1]
                delete_exif_data(target_image, "deleted_image.jpg")
                break

    if action is None:
        for image_path in sys.argv[1:]:
            try:
                image = Image.open(image_path)
                print(f"\n===\nImage: {image_path}")
                data = get_exif_data(image_path)
                if data:
                    print("\nEXIF metadata:")
                    get_creation_date(data)
                    print_data(data)
                else:
                    print("No EXIF metadata found.")
                print("===")
            except IOError:
                print(f"\nImage {image_path} can't be opened")


if __name__ == "__main__":
    main()