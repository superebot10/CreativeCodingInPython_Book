import time
import turtle
shelly = turtle.Turtle()
for n in range(36):
    for i in range(6):
        shelly.forward(100)
        shelly.left(60)
    shelly.right(10)


while True:
    a = input('Press "e" to exit.')
    if a == 'e':
        break