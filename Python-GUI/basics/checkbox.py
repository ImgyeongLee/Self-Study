from msilib.schema import CheckBox
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')
root.geometry("400x400")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

cbox = Checkbutton(root, text="Check this box, I dare you!", variable=var, onvalue="On", offvalue="Off")
cbox.deselect()
cbox.pack()

btn = Button(root, text="Show Selection", command=show).pack()

root.mainloop()