#!/usr/bin/python3
import calculator_1
from sys import argv


def main():
    if (len(argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if argv[2] == '+':
        print("{} + {} = {}".format(argv[1], argv[3],
                                    calculator_1.add(int(argv[1]),
                                    int(argv[3]))))
    elif argv[2] == '-':
        print("{} - {} = {}".format(argv[1], argv[3],
                                    calculator_1.sub(int(argv[1]),
                                    int(argv[3]))))
    elif argv[2] == '*':
        print("{} * {} = {}".format(argv[1], argv[3],
                                    calculator_1.mul(int(argv[1]),
                                    int(argv[3]))))
    elif argv[2] == '/':
        print("{} / {} = {}".format(argv[1], argv[3],
                                    calculator_1.div(int(argv[1]),
                                    int(argv[3]))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
