import random
from word_list import word_list 
from logo import stages, logo


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(f'{logo}\n')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(f"{' '.join(display)} ({word_length} characters)\n")
  
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if len(guess) != word_length:
        while len(guess) != word_length:
            guess = input("Invalid length. Try to enter your input again: ").lower()
    
    for i in range(word_length):
        if guess[i] == chosen_word[i]:
            display[i] = chosen_word[i]
      
    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
      
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    
    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
      
    print(stages[lives])
    
print(f"The answer was: {chosen_word}")