import random

import hangman_words

import hangman_art

from hangman_words import word_list
from hangman_art import logo, stages

print(logo)


chosen_word = random.choice(word_list)

# Set lives to 6
lives = 6

# Testing code
print(f'Psst, the solution is {chosen_word}')

# an empty list called display
display = []
for letter in chosen_word:
    display.append("_")

print(display)

while "_" in display and lives > 0:
    guess = input("Choose an alphabet to make a guess: ").lower()

    #If the letter is already guessed print message as "Already Guessed, pick another letter"
    if guess in display:
        print("Already Guessed, pick another letter")
    # Loop through each position in the chosen_word;
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    # Check if guess is not a letter in chosen_word and reduce lives by 1
    if guess not in chosen_word:
        print(f"The letter '{guess}' is not in the word")
        lives -= 1
        print(stages[lives])  # Print corresponding hangman stage
        
    print(" ".join(display))  # Print the display with revealed letters

    

# Print "You Win" if the user has correctly guessed the word
if "_" not in display:
    print("You Win!")
else:
    print("You lose!")