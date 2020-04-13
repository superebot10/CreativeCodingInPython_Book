import turtle
import time
import random

def square(s):
    for i in range(4):
        shelly.forward(s)
        shelly.left(90)

shelly = turtle.Turtle()

colors = ['red', 'blue', 'yellow', 'green', 'black']
shelly.shape('turtle')
for i in range(5000):
    pos = shelly.position()
    x = pos[0]
    y = pos[1]
    shelly.speed(10)
    shelly.forward(random.randint(1,20))
    shelly.begin_fill()
    shelly.color(colors[random.randint(0,4)])
    square(random.randint(10, 50))
    shelly.end_fill()
    shelly.forward(random.randint(20, 100))
    shelly.right(random.randint(0, 360))
    shelly.begin_fill()
    shelly.color(colors[random.randint(0, 4)])
    shelly.speed(10)
    shelly.circle(random.randint(5, 30))
    shelly.end_fill()
    shelly.left(random.randint(0, 360))
    if x > 715 or x < -715 or y > 400 or y < -400:
        shelly.penup()
        shelly.goto(random.randint(-715, 715), random.randint(-400, 400))
        shelly.pendown()


while True:
    a = input('Press "e" to exit.')
    if a == 'e':
        break