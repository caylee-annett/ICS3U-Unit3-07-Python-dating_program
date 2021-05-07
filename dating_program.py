#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program uses 'and' and tells the user if they are the right age to
#   date someone's grandchild


def main():
    # This function tells the user if they can date the grandchild

    # Input
    print("This program will tell you if you can date my grandchild.")
    print("")
    age_as_string = input("Please enter your age: ")

    # Process & Output
    try:
        age_as_integer = int(age_as_string)

        if age_as_integer > 25 and age_as_integer < 40:
            print("You are allowed to date my grandchild.")
        elif age_as_integer <= 25:
            print("Sorry, you're too young!")
        elif age_as_integer >= 40:
            print("You're too old!")
    except Exception:
        print("{} is not a valid input.".format(age_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
