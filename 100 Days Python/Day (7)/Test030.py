#Step 1
import random

word_list = ["ardvark", "baboon", "camel"]

#randomly choose a word from list and assign it to a variable called chosen_word

chosen_word = random.choice(word_list)

#ask the use to guess a letter and assign their answer to a variable called guess. Make guess lowercase

guess = input(str("Choose an alphabet to start your guess: ").lower())

#check if the letter the user guessed (guess) is one of the letter in the chosen word

for letter in chosen_word:
    if letter == guess:
        print("Correct")
    else:
        print("Wrong")
