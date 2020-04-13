from tkinter import *
import random


window = Tk()
window.title('My first GUI (Don\'t listen to the other ones. They are LIARS)')

def blue_rect_move(event):
    key = event.keysym
    if key == "/":
        canvas.move(blue_rect,0,10)

def hello_function():
    print('I YEET THINGS!!!!!!!!!!!')
    display_area.config(text = 'I YEET THINGS!!!!!!!!!!!', fg="yellow", bg="black")

# move circle to left or right
def move_circle(event):
    key = event.keysym
    if key == "Right":
        canvas.move(circle,10,0) # change x
    elif key == "Left":
        canvas.move(circle,-10,0) # change x
    elif key == "Up":
        canvas.move(circle, 0, -10)
    elif key == "Down":
        canvas.move(circle, 0, 10)

# function that handles mouse clicks on the character mychar
def move_character(event):
     canvas.coords(mychar,event.x,event.y)


button1 = Button(window, text="Click to yeet a chair", command = hello_function)
button1.pack()

display_area = Label(window, text="")
display_area.pack()

canvas = Canvas(window, width=4000, height=4000)
canvas.pack()

circle = canvas.create_oval(100,200,130,230, fill = 'red')

blue_rect = canvas.create_rectangle(50,50,70,80, fill = 'blue')

screen_message  = canvas.create_text(670,200, text = 'Welcome', fill = 'black', font = ('Helvetica', 30))

img = PhotoImage(file="greenChar.gif")
mychar = canvas.create_image(100,100,image = img)

# bind keyboard input to move_circle
canvas.bind_all('<Key>', move_circle)
# bind left button mouse to moving the character
canvas.bind_all('<Button-1>', move_character)

window.mainloop()