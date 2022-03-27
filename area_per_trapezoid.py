#!/usr/bin/env python3

# Created by: Sarah
# Created on: Mar 26, 2022
# This program asks the user for the bases and side lengths
# of a trapezoid. It then calculates and
# displays the area and perimeter.
import math


def main():
    # get the user input, base1, base2, and the height
    print("Today, we will be calculating the area")
    print("and perimeter of a trapezoid")
    base1 = float(input("Enter base-1 of the trapezoid (cm): "))
    base2 = float(input("Enter base-2 of the trapezoid (cm): "))
    height = float(input("Enter the height of the trapezoid (cm): "))

    # calculate the area of the trapezoid
    area = height*(base1 + base2)/2

    # display the area to the user
    print("")
    print("\033[1;96mArea = {:,.2f} cm^2".format(area))
    print("")

    # get side_c and side_d in order to calculate the perimeter
    print("Now, we will calculate the perimeter: ")
    side_c = float(input("Enter the side length C of the trapezoid (cm): "))
    side_d = float(input("Enter the side length D of the trapezoid (cm): "))

    # calculate the perimeter of the trapezoid
    perimeter = base1 + base2 + side_c + side_d

    # display the perimeter to the user
    print("")
    print("\033[1;95mPerimeter = {:,.2f} cm".format(perimeter))


if __name__ == "__main__":
    main()
