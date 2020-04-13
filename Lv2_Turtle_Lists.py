import turtle
import time
shelly = turtle.Turtle()
colors = ['red', 'green', 'blue']
print(colors[0])
print(colors[1])
shelly.color(colors[0])

shelly = turtle.Turtle()
colors = ['red', 'green', 'blue']
for i in range(3):
    shelly.color(colors[i])
    shelly.forward(50)
    print(colors[i])



time.sleep(3)