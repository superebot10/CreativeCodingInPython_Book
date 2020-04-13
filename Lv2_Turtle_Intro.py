import turtle
import time

shelly = turtle.Turtle()

shelly.shape('turtle')
shelly.forward(100)
shelly.right(90)
shelly.left(60)
shelly.backward(100)
shelly.color('red')
shelly.circle(10)
shelly.penup()
shelly.pendown
shelly.goto(35, 80)
shelly.hideturtle

for i in range(4):
    shelly.color('blue')
    shelly.pendown()
    shelly.forward(100)
    shelly.left(90)
    print(i)

time.sleep(3)