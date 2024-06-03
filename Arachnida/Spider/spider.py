import argparse

def parse_arguments():
    parser = argparse.ArgumentParser("Spider program to download images")
    parser.add_argument('-r', '--recursive', action="store_true", help="Recursive Download")
    parser.add_argument('-l', '--level', type=int, default=5, help="Depth level of the recursive download")
    parser.add_argument('-p', '--path', default='./data/', help="Path of downloaded files")
    parser.add_argument('URL', help="URL targeted")
    return parser.parse_args()

def main():
    args = parse_arguments()
    print(args.recursive)
    print(args.level)
    print(args.path)
    print(args.URL)


if __name__ == "__main__":
    main()