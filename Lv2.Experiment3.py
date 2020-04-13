import turtle
import time

shelly = turtle.Turtle()

#green circle
shelly.penup()
shelly.goto(-30, 10)
shelly.pendown()
shelly.begin_fill()
shelly.color('green')
shelly.circle(150)
shelly.end_fill()

#eye1
shelly.goto(-75, 160)
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()

shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()
shelly.penup()

#eye2
shelly.goto(0, 160)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()

shelly

time.sleep(3)