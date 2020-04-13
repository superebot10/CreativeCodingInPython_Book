import turtle
import time

shelly = turtle.Turtle()

turtle.bgcolor('black')
colors = ['red','green', 'blue', 'orange', \
     'purple', 'yellow']
for i in range(6):
    shelly.color(colors[i])
    for n in range(4):
        shelly.forward(20)
        shelly.left(90)
    shelly.penup()
    shelly.forward(30)
    shelly.pendown()
shelly.hideturtle()

time.sleep(3)