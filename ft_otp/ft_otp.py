#!/usr/bin/env python3

import os, argparse

def parse_arguments():
    parser = argparse.ArgumentParser("OTP Algorithm")
    parser.add_argument('-g', '--get_key', action="store_true", help="Get an hexadecimal key")
    parser.add_argument('-k', '--key_use', action="store_true", help="Create a password with the key")
    parser.add_argument('file', help="key file")
    return parser.parse_args()


def main():
    args = parse_arguments()

    if not args.file:
        print("Usage: ./ft_otp.py [OPTION] [FILE]")
    elif args.get_key is not True and args.key_use is not True:
        print("Usage: ./ft_otp.py [OPTION] [FILE]")
    else:
        print("OK")


if __name__ == "__main__":
    main()