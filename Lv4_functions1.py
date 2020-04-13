import turtle
import time
shelly = turtle.Turtle()

def square(s):
    for i in range(4):
        shelly.forward(s)
        shelly.left(90)

square(100)
shelly.forward(100)
square(200)
shelly.forward(100)
square(300)