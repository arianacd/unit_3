# by Ariana Daney
# last modified 1, october 2019
# this program calculates the area of a rectangular prism where the user gives the measurements


def instructions():
    """
    this function tells the user what the program does
    :return: none
    """
    print("this function will calculate the area of a rectangular prism")
    print("please enter width, length, and height")


def user_width():
    """
    this function gets the users chosen width
    :return: the users given width
    """
    return float(input("width:"))


def user_length():
    """
    this function gets the users chosen length
    :return: the users given length
    """
    return float(input("length:"))


def user_height():
    """
    this function gets the users chosen height
    :return: the users given height
    """
    return float(input("height:"))


def area_of_rectangle(length, width):
    """
    this function calculates the area of a rectangle
    :param length: the length of the rectangle
    :param width: the width of the rectangle
    :return: the length times the width
    """
    return length * width


def surface_area(length, width, height):
    """
    this function calculates the total surface area of the rectangular prism
    :param length: the length of the rectangle
    :param width: the width of the rectangle
    :param height: the height of the rectangle
    :return: the sides times two, all added together
    """
    return (area_of_rectangle(length, width) * 2) + (area_of_rectangle(length, height) * 2) + \
           (area_of_rectangle(width, height) * 2)


def main():
    instructions()
    width = user_width()
    length = user_length()
    height = user_height()
    print("the total surface area is", surface_area(width, length, height))


main()
