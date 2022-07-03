from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

r = IntVar()
myLabel = Label(root, text=r.get())

# You can set the value of the variable like this:
# r.set("2")

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode, command=lambda: clicked(pizza.get())).pack(anchor=W)

def clicked(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text=value)
    myLabel.pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

myLabel.pack()

root.mainloop()