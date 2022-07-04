from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

def open():
    top = Toplevel()
    Label(top, text="Hello World").pack()
    
btn = Button(root, text="Open Second Window", command=open).pack()

mainloop()