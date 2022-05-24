import turtle
from turtle import Turtle, Screen
from random import choice, randint

timmy = Turtle()
turtle.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)

directions = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(15)

for _ in range(150):
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(choice(directions))

exit_when = Screen()
exit_when.exitonclick()

