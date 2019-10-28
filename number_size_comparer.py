#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program determines which number is larger between two numbers


def main():

    # input Process and Output
    try:
        # input
        user_number1 = int(input("Enter your first number: "))
        user_number2 = int(input("Enter your second number: "))

        # process and output
        if (user_number1 > user_number2):
            print("The first number: " + str(user_number1))
            print("is larger than the second number: " + str(user_number2))
        elif (user_number1 < user_number2):
            print("The second number: " + str(user_number2))
            print("is larger than the first number: " + str(user_number1))
        else:
            print("Both numbers are equivalent")
    except Exception:
        print("Please input only valid integers")


if __name__ == "__main__":
    main()
