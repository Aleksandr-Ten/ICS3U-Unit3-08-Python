#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: March 2022
# This program tells if it is a leap year


def main():
    # this function calculates the leap year
    
    # input
    year_number_string = input("Enter the year: ")
    
    # process & output
    try:
        year_number = int(year_number_string)
        if year_number % 4 == 0:
            if year_number % 100 == 0:
                if year_number % 400 == 0:
                    print("It is a leap year")
                else:
                    print("It is not a leap year")
            else:
                print("It is a leap year")
        else:
            print("It is not a leap year")
    except Exception:
        print("Invalid input. Please try again.")
    finally:
        print("\nDone")


if __name__ == "__main__":
    main()

