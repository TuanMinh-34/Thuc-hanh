
print("############################")
import turtle

import turtle
colors = ["red", "blue", "green", "red", "blue", "green", "red", "blue", "green", "red", "blue", "green"]
painter = turtle.Turtle()
painter.pensize(3)
angle = 360 / len(colors) # Góc xoay giữa các hình

for color in colors:
    painter.pencolor(color)
    painter.circle(100)
    painter.left(angle)

turtle.done()
