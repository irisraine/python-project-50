#!/usr/bin/env python

import argparse
from gendiff import generate_diff
from gendiff.format import stylish
from gendiff.parse import load_content

FORMATTERS = {
    "STYLISH": stylish,
}


def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f",
        "--format",
        default="STYLISH",
        help="set format of output"
    )
    args = parser.parse_args()
    contents1 = load_content(args.first_file)
    contents2 = load_content(args.second_file)

    print()
    print(FORMATTERS[args.format](generate_diff(contents1, contents2)))


if __name__ == '__main__':
    main()
