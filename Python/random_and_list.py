import random

# a >= 1 and a <= 10
random_integer = random.randint(1, 10)
print(random_integer)

# 0.000000 to 9.999999...
random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

coin = random.randint(0, 1)
if coin == 0:
    print("Tails")
else:
    print("Heads")
    
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
name_result = random.randint(0, len(names) - 1)
print(f"Result: {names[name_result]}")

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# The way to access is similar to dealing with a 2D array
dirty_dozen = [fruits, vegetables]

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0])
vertical = int(position[1])

map[horizonal][vertical] = 'X'

print(f"{row1}\n{row2}\n{row3}")