#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 03 27, 2025
# This program is hardcore number guessing game with try catch.

import random


def main():

    # Gets the input number from user
    user_number = input("Insert random number from 0 to 9")
    print("")
    # Generates random number
    computer_number = random.randint(0, 9)
    try:
        user_number = int(user_number)
        if user_number == computer_number:
            print("You won.")
        elif user_number != computer_number:
            print("You lost the number is, {}".format(computer_number))
    except Exception:
        print("Enter correct input.")
    finally:
        print("Thanks for gamble.")


if __name__ == "__main__":
    main()
