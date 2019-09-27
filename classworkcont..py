# by ariana daney
# last edited on 26, september 2019
# daily exercises
import math


def triangle_area(num1, num2, num3):
    s = (num1 + num2 + num3) / 2
    a = math.sqrt(s * (s - num1) * (s - num2) * (s - num3))
    return a


def main():
    a = int(input("what is the length of the first side"))
    b = int(input("what is the length of the second side"))
    c = int(input("what is the length of the third side"))
    answer = triangle_area(a, b, c)
    print("the area of the triangle is", answer)


main()
