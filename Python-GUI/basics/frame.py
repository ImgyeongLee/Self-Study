from ast import Lambda
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

# inside of the frame
frame = LabelFrame(root, text="This is my Frame...", padx=50, pady=50)
# outside of the frame
frame.pack(padx=10, pady=10)

b = Button(frame, text="Do not Click Here!")
b2 = Button(frame, text="...or here!")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()