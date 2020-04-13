import time
import turtle
colors = ['red', 'green', 'orange', 'blue', \
    'yellow', 'red']
shelly = turtle.Turtle()
turtle.bgcolor('black')
for n in range(36):
    for i in range(6):
        shelly.color(colors[i])
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)
shelly.penup()
shelly.color('white')
for i in range(36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(5)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)
shelly.hideturtle()

while True:
    a = input('Press "e" to exit.')
    if a == 'e':
        break