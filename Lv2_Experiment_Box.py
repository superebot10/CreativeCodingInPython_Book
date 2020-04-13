import turtle
import time

shelly = turtle.Turtle()
line = 2

color_pos = 0
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle.bgcolor('black')

for i in range(1000):
    shelly.color(colors[color_pos])
    color_pos = color_pos + 1
    if color_pos > 5:
        color_pos = 0
    shelly.forward(line)
    shelly.right(90)
    line = line + 2


while True:
    a = input('Press "e" to exit.')
    if a == 'e':
        break