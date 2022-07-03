from ast import Lambda
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

my_img1 = ImageTk.PhotoImage(Image.open("ben.png"))
my_img2 = ImageTk.PhotoImage(Image.open("hanon.png"))
my_img3 = ImageTk.PhotoImage(Image.open("trash.png"))

image_list = [my_img1, my_img2, my_img3]

# bd - border
# relief=TYPE - kind of style
# anchor=POS - place the object
status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def button_work(cmd, image_number):
    global my_label
    global button_next
    global button_back
    global status
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number - 1])
    button_next = Button(root, text=">>", command=lambda: button_work("next", image_number + 1))
    button_back = Button(root, text="<<", command=lambda: button_work("back", image_number - 1))
    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    
    if image_number == 3 and cmd == "next":
        button_next = Button(root, text=">>", state=DISABLED)
    if image_number == 1 and cmd == "back":
        button_back = Button(root, text="<<", state=DISABLED)
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_next.grid(row=1, column=2)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

button_back = Button(root, text="<<", command=lambda: button_work, state=DISABLED)
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_next = Button(root, text=">>", command=lambda: button_work("next", 2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_next.grid(row=1, column=2)
# sticky=POS+POS : stretch
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()