from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
shape = {
    3: 120,
    4: 90,
    5: 72,
    6: 60,
    7: 360/7,
    8: 360/8,
    9: 360/9,
    10: 36
}

for x, y in shape.items():
    for _ in range(x):
        timmy.forward(100)
        timmy.right(y)
    timmy.color(choice(colours))

screen_exit = Screen()
screen_exit.exitonclick()
