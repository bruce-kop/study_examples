import argparse
import sys

def main(args=sys.argv[1:]):

    print(args)
    parser = argparse.ArgumentParser(description='manul this script')

    parser.add_argument("--file", help='filename', type=str, default=None)
    parser.add_argument("--size", help='size', type=int, default=128)
    parser.add_argument("-b", help='b')

    args = parser.parse_args(args=args)
    print(args.file)
    print(args.size)
    print(args.b)


if __name__ == '__main__':
    main()