from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')
root.geometry("400x400")

# Drop Down Boxes

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = ["Monday",
           "Tuesday",
           "Wednesday",
           "Thursday",
           "Friday"]

clicked = StringVar()
clicked.set(options[0])

# If you do not put * in front of the list name, it works weird.
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Show Selection", command=show).pack()

root.mainloop()