#Guessing the number
import random

EASY_TURNS = 10
HARD_TURNS = 5


#Choice checking function between user and computer
def check_choice(user_choice, comp_choice, turns):
    ''' Checks choice on the user vs computer and returns the turns remaining'''
    if user_choice < comp_choice:
        print("Your choice is too low. Guess high") 
        return turns - 1
    elif user_choice > comp_choice:
        print("Your number is too high. Guess low")
        return turns - 1
    elif user_choice == comp_choice:
        print(f"Your choice is correct, it is {comp_choice}")

#Setting difficulting to make the number of guess in the game
def set_difficulty():
    level = input("Choose your difficulty level. Type 'e' for easy or 'h' for hard: ")
    if level == "e":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game_start():
    print('''
     _    _          _        ____                        ____                       
    / \  | |__   ___( )___   / ___|_   _  ___  ___ ___   / ___| __ _ _ __ ___   ___  
   / _ \ | '_ \ / _ \// __| | |  _| | | |/ _ \/ __/ __| | |  _ / _` | '_ ` _ \ / _ \ 
  / ___ \| |_) |  __/ \__ \ | |_| | |_| |  __/\__ \__ \ | |_| | (_| | | | | | |  __/ 
 /_/   \_\_.__/ \___| |___/  \____|\__,_|\___||___/___/  \____|\__,_|_| |_| |_|\___| 
                                                                                     
''')
    comp_choice = int(random.choice(range(0, 101)))
    print("Welcome to the number guessing game")
    print("Computer: 'I think of a number between 1 to 100.' ")

    print(f"Play test: {comp_choice}")

    turns = set_difficulty()

    user_choice = 0
    #Repeating the game until the answer or choice runs out
    while user_choice != comp_choice:
        print(f"You have {turns} attempts remaining to guess the number")
        user_choice = int(input("Guess the number between 1 to 100: "))
        
        turns = check_choice(user_choice, comp_choice,turns)

        if turns == 0:
            print(f"Computer: Sorry! the choice I made was {comp_choice} You lost! ")
            return

game_start()



    
