# The game of Higher Lower 
import os
import random
from art import logo
from art import vs

print(logo)

def clear_screen():
    os.system('cls')

# Step 2: Prepare celebrity data
# Create a list of dictionaries, each containing information about a celebrity (name, follower_count, description, country)
from game_data import data 

def get_highest_follower(celebrity_a, celebrity_b):
    """Compares follower counts of two celebrities and returns 'a' or 'b'."""
    if int(celebrity_a['follower_count']) > int(celebrity_b['follower_count']):
        return 'a'
    else:
        return 'b'
    
def correct_response(player_guess, correct_answer, celebrity_a, celebrity_b):
    if player_guess == correct_answer:
            print("That's right! You guessed correctly.")
            return celebrity_a if correct_answer == 'a' else celebrity_b
    else:
            print(f"Wrong. The correct answer was {correct_answer}.")

def game_start():
    while True:
        celebrity_a = random.choice(data)
        celebrity_b = random.choice(data)

        while celebrity_a == celebrity_b:
            celebrity_b = random.choice(data)

        print(f"The celebrity A is {celebrity_a['name']} who is a {celebrity_a['description']} from {celebrity_a['country']}")
        print(vs)
        print(f"The celebrity B is {celebrity_b['name']} who is a {celebrity_b['description']} from {celebrity_b['country']}")

        insta_count_a = int(celebrity_a['follower_count'])
        insta_count_b = int(celebrity_b['follower_count'])

        while True:
            player_guess = input(f"Guess the celebrity with the highest Instagram followers. Enter 'a' for {celebrity_a['name']} or 'b' for {celebrity_b['name']} ")
            
            if player_guess == 'a' or player_guess == 'b':
                break
            else:
                print("Invalid input. Please enter 'a' or 'b'.")

        correct_answer = get_highest_follower(celebrity_a, celebrity_b)
        celebrity_c = None  # Initialize celebrity_c

        celebrity_c = correct_response(player_guess, correct_answer, celebrity_a, celebrity_b)

        if celebrity_c is not None:
            play_again = input(f"Do you want to continue with {celebrity_c['name']}'s comparison? 'y' for yes. 'n' for no: ")
        else:
            play_again = input("Do you want to play again? 'y' for yes. 'n' for no: ")

        clear_screen()
        if play_again.lower() != 'y':
            print("Thanks for playing the game!")
            break



# Step 11: Call the game loop
# Call the function or start the loop to run the game
game_start()
