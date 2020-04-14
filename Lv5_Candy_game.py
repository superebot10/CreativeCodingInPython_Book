# The Yummyness Game game program
from tkinter import *
import random

# make window
window = Tk()
window.title('The Yummyness Game')

# create a canvas to put objects on the screen
canvas = Canvas(window, width=1000, height=500, bg = 'black')
canvas.pack()

# set up welcome screen with title and directions
title = canvas.create_text(500, 200, text='The Yummieness Monster', fill='white', font=('Helvetica', 30))
directions = canvas.create_text(500, 300, text= 'Collect candy but avoid the red ones.', fill='white', font=('Helvetica', 20))

# set up score display usin label widget
score = 0
score_display = Label(window, text="Score: " + str(score))
score_display.pack()

# set up level display using label widget
level = 1
level_display = Label(window, text="Level: " + str(level))
level_display.pack()

# create an image object using the gif file
player_image = PhotoImage(file="greenChar.gif")
# use image object to create a character at position 500, 480
mychar = canvas.create_image(500, 480, image = player_image)

# variables and lists needed for managing candy
candy_list = [] # list containing all candy created, empty at start
bad_candy_list = [] # list containing all bad candy created, empty at start
candy_speed = 2 # iniial speed of falling candy
candy_color_list = ['red', 'yellow', 'blue', 'green', 'purple', 'pink', 'white']

# function to make candy at random places
def make_candy():
    # pick a random x position
    xposition = random.randint(1, 400)
    # pick a random color
    candy_color = random.choice(candy_color_list)
    # create a candy of size 30 at random position and color
    candy = canvas.create_oval(xposition, 0, xposition+30, 30, fill = candy_color)
    # add candy to list
    candy_list.append(candy)
    # if color of candy is red - add it to bad_candy_list
    if candy_color == 'red':
        bad_candy_list.append(candy)
    # schedule this function to make candy again
    window.after(1000, make_candy)

# function moves candy downwards, and schedules call to move_candy
def move_candy():
    # loop through list of candy and change y position
    for candy in candy_list:
        canvas

window.mainloop()