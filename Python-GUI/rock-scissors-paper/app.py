from tkinter import *
import random

root = Tk()
root.title("Rock Scissors Paper - Imgyeong Lee")
root.iconbitmap('./sairan.ico')

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, scissors, paper]
randnum = random.randint(0, 2)

def game(selection):
    Label(root, text=game_images[selection]).grid(row=4, column=0)
    Label(root, text="VS").grid(row=4, column=1)
    Label(root, text=game_images[randnum]).grid(row=4, column=2)
    Button(root, text="Rock", padx=40, pady=10, command=lambda: game(0), state=DISABLED).grid(row=2, column=0)
    Button(root, text="Scissors", padx=40, pady=10, command=lambda: game(1), state=DISABLED).grid(row=2, column=1)
    Button(root, text="Paper", padx=40, pady=10, command=lambda: game(2), state=DISABLED).grid(row=2, column=2)
    
    if (randnum == 0 and selection == 1) or (randnum == 1 and selection == 2) or (randnum == 2 and selection == 0):
        Label(root, text="LOSE").grid(row=5, column=0, columnspan=3)
    elif (selection == 0 and randnum == 1) or (selection == 1 and randnum == 2) or (selection == 2 and randnum == 0):
        Label(root, text="YOU WON THE GAME!").grid(row=5, column=0, columnspan=3)
    else:
        Label(root, text="TIE").grid(row=5, column=0, columnspan=3)
        

greeting = Label(root, text="What do you want to pick up?").grid(row=0, column=0, columnspan=3)
Label(root, text="---------------").grid(row=1, column=0, columnspan=3)
sel1 = Button(root, text="Rock", padx=40, pady=10, command=lambda: game(0)).grid(row=2, column=0)
sel2 = Button(root, text="Scissors", padx=40, pady=10, command=lambda: game(1)).grid(row=2, column=1)
sel3 = Button(root, text="Paper", padx=40, pady=10, command=lambda: game(2)).grid(row=2, column=2)
Label(root, text="---------------").grid(row=3, column=0, columnspan=3)


root.mainloop()
