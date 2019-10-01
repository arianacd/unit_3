# by Ariana Daney
# last modified 1, october 2019
# this program calculates the area of a rectangular prism where the user gives the measurements


def instructions():
    print("this function will calculate the area of a rectangular prism")
    print("please enter width, length, and height")


def user_width():
    width = float(int("width:"))
    return width


def user_length():
    length = float(int("length:"))
    return length


def user_height():
    height = float(int("height:"))
    return height


def area_of_rectangle(length, width):
    area = length * width
    return area


def surface_area(height, length, width):
    surface = height * length * width
    return surface


def main():
    instructions()
    area = user_length(), user_width()
    surface = user_width(), user_length(), user_height()






main()