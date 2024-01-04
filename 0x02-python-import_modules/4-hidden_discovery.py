#!/usr/bin/python3
import hidden_4


def main():
    names_list = dir(hidden_4)

    for name in names_list:
        if name[0] != '_' and name[1] != '_':
            print(name)


if __name__ == "__main__":
    main()
