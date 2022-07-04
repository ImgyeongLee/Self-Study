from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

def open():
    global my_image
    # Get the file address
    root.filename = filedialog.askopenfilename(initialdir="./", title="Select A File", filetypes=(("png files", "*.png"),("all files", "*.*")))
    my_label = Label(root, text=root.filename).pack()
    # Show the image
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()