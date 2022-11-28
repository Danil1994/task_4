import argparse

from collection_framework import count_unical_symbol
from exception import FileDoesNotExist, NotArgument


def read_file(file_name: str) -> str:
    try:
        with open(file_name, 'r') as file_:
            return file_.read()
    except FileNotFoundError:
        raise FileDoesNotExist("The specified file does not exist")


def parser() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--string', required=False)
    parser.add_argument('--file', required=False)
    obj = parser.parse_args()

    if obj.file is None and obj.string is None:
        raise NotArgument("Use '--string' or '--file command'")

    elif obj.file:
        return count_unical_symbol(read_file(obj.file))

    else:
        return count_unical_symbol(obj.string)


if __name__ == '__main__':
    print(parser())
