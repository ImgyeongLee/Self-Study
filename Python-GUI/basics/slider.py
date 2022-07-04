from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')
root.geometry("400x400")

def slide():
    Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()

my_btn = Button(root, text="Text Update", command=slide).pack()

root.mainloop()