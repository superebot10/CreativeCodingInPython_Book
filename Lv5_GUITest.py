from tkinter import *

window = Tk()
window.title('My first GUI')

def hello_function():
    print('Hello, World!')
    display_area.config(text = 'Hello, World', fg ="yellow", bg = "black")

# adding a button widget
button1 = Button(window, text = "Click me", command = hello_function)
button1.pack()

# adding the display area- using the label widget
display_area = Label(window, text ="")
display_area.pack()

window.mainloop()

#Top Secret Code: 123ABC