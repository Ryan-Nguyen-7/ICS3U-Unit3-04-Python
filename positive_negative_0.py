#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on December 2020
# This program asks the user for a number and
#   checks if it is positive, negative, or 0


def main():
    # input
    input_value = int(input("Enter number: "))
    print("")

    # process + output
    if input_value < 0:
        print("-")
    elif input_value == 0:
        print(0)
    else:
        print("+")


if __name__ == "__main__":
    main()
