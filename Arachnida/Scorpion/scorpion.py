#!/usr/bin/env python3

import sys
from PIL import Image

def main():
    with open('./scorpion.txt', 'r') as fichier:
        contenu = fichier.read()
        print(contenu)

if __name__ == "__main__":
    main()