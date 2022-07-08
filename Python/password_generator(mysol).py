import random

from sqlalchemy import null
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_elements = []
password = ""

for _ in range(nr_letters):
    idx = random.randint(0, len(letters) - 1)
    password_elements.append(letters[idx])

for _ in range(nr_symbols):
    idx = random.randint(0, len(symbols) - 1)
    password_elements.append(symbols[idx])

for _ in range(nr_numbers):
    idx = random.randint(0, len(numbers) - 1)
    password_elements.append(numbers[idx])

while (len(password_elements) != len(password)):
    idx = random.randint(0, len(password_elements) - 1)
    if password_elements[idx] != null:
        password += password_elements[idx]
        password_elements[idx] = null

print(password)