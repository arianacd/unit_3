# by Ariana daney
# last modified september 27, 2019
# creating a font

import turtle
turtle.speed(0)


def invisible_move(num1, num2):
    turtle.penup()
    turtle.goto(num1, num2)
    turtle.pendown()


def letter_m():
    turtle.color("hot pink")
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


def letter_p():
    turtle.seth(90)
    turtle.fd(50)
    turtle.right(90)
    turtle.fd(28)
    turtle.right(90)
    turtle.fd(14)
    turtle.right(90)
    turtle.fd(28)


def main():
    invisible_move(-400, 0)
    letter_m()
    invisible_move(-350, 0)
    letter_i()
    invisible_move(-328, 0)
    letter_s()
    invisible_move(-278, 0)
    letter_s()
    invisible_move(-228, 0)
    letter_i()
    invisible_move(-206, 0)
    letter_s()
    invisible_move(-156, 0)
    letter_s()
    invisible_move(-106, 0)
    letter_i()
    invisible_move(-84, 0)
    letter_p()
    invisible_move(-34, 0)
    letter_p()
    invisible_move(16, 0)
    letter_i()
    invisible_move(20, 0)
    turtle.hideturtle()


main()


turtle.exitonclick()