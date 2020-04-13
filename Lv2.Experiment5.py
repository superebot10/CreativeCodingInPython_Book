import turtle
import time

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
shelly = turtle.Turtle()

turtle.bgcolor('black')

for i in range(36):
    shelly.penup()
    shelly.forward(200)
    for n in range(6):
        shelly.color(colors[n])
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.backward(20)
    shelly.backward(80)
    shelly.right(10)

while True:
    a = input('Press "e" to exit.')
    if a == 'e':
        break