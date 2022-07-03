from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Learn Tkinter! - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup(type):
    # (Title of the messagebox, Content)
    
    if type == 0:
        messagebox.showinfo("This is my Popup!", "Hello World!")
    elif type == 1:
        messagebox.showwarning("This is my Popup!", "Hello World!")
    elif type == 2:
        messagebox.showerror("This is my Popup!", "Hello World!")
    elif type == 3:
        result = messagebox.askquestion("This is my Popup!", "Hello World!")
        if result == "yes":
            Label(root, text="You clicked yes!").pack()
        else:
            Label(root, text="You clicked no!").pack()
    elif type == 4:
        result =  messagebox.askokcancel("This is my Popup!", "Hello World!")
        if result == 1:
            Label(root, text="You clicked yes!").pack()
        else:
            Label(root, text="You clicked no!").pack()
    elif type == 5:
        result =  messagebox.askyesno("This is my Popup!", "Hello World!")
        if result == 1:
            Label(root, text="You clicked yes!").pack()
        else:
            Label(root, text="You clicked no!").pack()

Button(root, text="Show Info", command=lambda: popup(0)).pack()
Button(root, text="Show Warning", command=lambda: popup(1)).pack()
Button(root, text="Show Error", command=lambda: popup(2)).pack()
Button(root, text="Ask question", command=lambda: popup(3)).pack()
Button(root, text="Ask Cancel OK", command=lambda: popup(4)).pack()
Button(root, text="Ask Yes No", command=lambda: popup(5)).pack()


root.mainloop()