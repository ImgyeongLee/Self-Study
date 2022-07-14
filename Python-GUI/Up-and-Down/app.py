import random
from tkinter import *
from logo import up, down, win, lose

root = Tk()
root.title("Up and Down - Imgyeong Lee")
root.iconbitmap('./sairan.ico')
root.geometry("600x600")

player_count = 8

# Play the game
def set_game():
    # Erase a frame
    global opening, root
    opening.destroy()
    
    # Pick a random number
    answer = random.randint(0, 100)
    
    # Initialize a game
    input_area = LabelFrame(root, text="\nI am thinking about one specific number. Guess it!", padx=50, pady=50)
    input_area.pack()
    desc = Label(input_area, text="Enter the number from 0 to 100")
    desc.pack()
    inputfield = Entry(input_area, width=30)
    
    inputfield.pack()
    
    # Print the player's life
    status = LabelFrame(root, text="\nYour Status", padx=60, pady=10)
    status.pack()
    player_heart = Label(status, text=f"Life: {str(player_count)}")
    player_heart.pack()
    res = Label(root, text=" ")
    res.pack()
    
    # Compare the input with the answer
    def compare():        
        if inputfield.get() != "":
            num = int(inputfield.get())
        else:
            return
        
        global player_count
        
        if num < answer:
            player_count -= 1
            player_heart.configure(text=f"Life: {str(player_count)}") 
            res.configure(text=up) 
            
        elif num > answer:
            player_count -= 1
            player_heart.configure(text=f"Life: {str(player_count)}") 
            res.configure(text=down) 
        
        else:
            player_heart.configure(text=f"Life: {str(player_count)}") 
            res.configure(text=win)
            hit.pack_forget()
            close = Button(root, text="Quit", padx=15, pady=5, command=quit_game)
            close.pack()
        
        if player_count == 0:
            res.configure(text=lose)
            hit.pack_forget()
            close = Button(root, text="Quit", padx=15, pady=5, command=quit_game)
            close.pack()
        
        
    hit = Button(root, text="Confirm", padx=15, pady=5, command=compare)
    hit.pack()


# Destroy the root and stop running the program
def quit_game():
    global root
    root.destroy()


opening = LabelFrame(root, text="\nWelcome to Up and Down game!", padx=50, pady=50)
opening.pack()

greeting = Label(opening, text="Do you wanna play the game?\n ")
greeting.pack()

yes = Button(opening, text="Yes", padx=30, pady=20, command=set_game)
yes.pack(side="left")

no = Button(opening, text="No", padx=30, pady=20, command=quit_game)
no.pack(side="right")

root.mainloop()