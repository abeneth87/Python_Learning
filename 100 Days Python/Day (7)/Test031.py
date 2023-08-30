
import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
print(f'Psst, the solution is {chosen_word}')

#1- Create an empty list called display
#for each letter in the chosen word, add a "_" to 'display'
#So if the chosen_word was "apple", display should be ["_","_","_","_","_"]

display = []
for letter in chosen_word:
    display.append("_")

print(display)

while "_" in display: 
    guess = input(str("Choose an alphabet to start your guess: ").lower())
print(display)
#2- Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at the position
for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = letter

print(" ".join(display))

# for letter in chosen_word:
#     if letter == guess:
#         print("Correct")
#     else:
#         print("Wrong")

#3- print 'display and replace the _ with guess letter if right
print(display)
 
