import time
import turtle

shelly = turtle.Turtle()

turtle.bgcolor('red')
for i in range(36):
    shelly.circle(100)
    shelly.right(10)
shelly.penup()
shelly.color('white')
for n in range(36):
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