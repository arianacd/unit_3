# by Ariana daney
# last modified september 27, 2019
# creating a font

import turtle


def invisible_move(num1, num2):
    turtle.penup()
    turtle.goto(num1, num2)
    turtle.pendown()


def letter_m():
    turtle.seth(90)
    turtle.fd(50)
    turtle.right(135)
    turtle.forward(20)
    turtle.left(90)
    turtle.fd(20)
    turtle.seth(270)
    turtle.fd(50)


def letter_i():
    turtle.seth(90)
    turtle.fd(50)


def letter_s():
    turtle.seth(0)
    turtle.fd(28)
    turtle.left(90)
    turtle.fd(36)
    turtle.left(90)
    turtle.fd(28)
    turtle.right(90)
    turtle.fd(14)
    turtle.right(90)
    turtle.fd(28)


def letter_p



def main():
    invisible_move(-400, 0)
    letter_m()
    invisible_move(-350, 0)
    letter_i()
    invisible_move(-328, 0)
    letter_s()
    invisible_move(-278, 0)


main()


turtle.exitonclick()