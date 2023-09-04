import os
import random
from art import logo, vs
from game_data import data

def clear_screen():
    """Clears the console screen."""
    os.system('cls')

def display_celebrity_info(celebrity):
    """Displays information about a celebrity."""
    print(f"The celebrity is {celebrity['name']} who is a {celebrity['description']} from {celebrity['country']}")

def get_highest_follower(celebrity_a, celebrity_b):
    """Compares follower counts of two celebrities and returns 'a' or 'b'."""
    if int(celebrity_a['follower_count']) > int(celebrity_b['follower_count']):
        return 'a'
    else:
        return 'b'

def game_start():
    print(logo)

    while True:
        clear_screen()

        # Choose two random celebrities
        celebrity_a = random.choice(data)
        celebrity_b = random.choice(data)

        # Display celebrity information
        display_celebrity_info(celebrity_a)
        print(vs)
        display_celebrity_info(celebrity_b)

        # Get player's guess
        player_guess = input(f"Guess the celebrity with the highest Instagram followers. Enter 'a' for {celebrity_a['name']} or 'b' for {celebrity_b['name']} ")

        # Compare follower counts
        correct_answer = get_highest_follower(celebrity_a, celebrity_b)

        if player_guess == correct_answer:
            print("That's right! You guessed correctly.")
            celebrity_c = celebrity_a if correct_answer == 'a' else celebrity_b
        else:
            print(f"Wrong. The correct answer was {correct_answer}.")
            celebrity_c = celebrity_a if correct_answer == 'a' else celebrity_b

        # Ask if the player wants to play again
        play_again = input(f"Do you want to continue with {celebrity_c['name']}'s comparison? 'y' for yes. 'n' for no: ")

        if play_again.lower() != 'y':
            # End of game
            print("Thanks for playing the game!")
            break


if __name__ == "__main__":
    game_start()
