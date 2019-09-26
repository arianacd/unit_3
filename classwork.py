# by Ariana Daney
# last modified 25, 2019
# daily exercises


def make_top_of_a_hexagon():
    print("  ________ ")
    print(" /        \\")
    print("/          \\")


def make_bottom_of_a_hexagon():
    print("\\          /")
    print(" \\________/")


def make_quotes():
    print("-\"-\'-\"-\'-\"-\'-")


def happy_birthday(name):
    for y in range(2):
        print("Happy Birthday to you")
    print("Happy Birthday dear", name)
    print("Happy Birthday to you.")


def adding_numbers(number1, number2):
    print(number1, "+", number2, "=", number1 + number2)


def main():
    make_top_of_a_hexagon()
    make_bottom_of_a_hexagon()
    make_quotes()
    make_top_of_a_hexagon()
    make_bottom_of_a_hexagon()
    make_quotes()
    make_bottom_of_a_hexagon()
    make_top_of_a_hexagon()
    make_quotes()
    make_bottom_of_a_hexagon()
    happy_birthday("Liana and Allison")
    adding_numbers(4, 6)


main()


