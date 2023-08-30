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

#Write your code below this line 👇
import random
comp_choice = random.choice(["rock", "paper", "scissors"])

my_choice = input("Enter your choice: 'rock', 'paper', or 'scissors': ")

if my_choice == comp_choice:
    print("It's a draw!") 
elif my_choice == "rock":
    if comp_choice == "scissors":
        print("You win!")
    else:
        print("Computer wins!")
elif my_choice == "paper":
    if comp_choice == "rock":
        print("You win!")
    else:
        print("Computer wins!")
elif my_choice == "scissors":
    if comp_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")
else:
    print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

# Print the ASCII art of the choices
print("Computer chose:")
if comp_choice == "rock":
    print(rock)
elif comp_choice == "paper":
    print(paper)
else:
    print(scissors)

print("You chose:")
if my_choice == "rock":
    print(rock)
elif my_choice == "paper":
    print(paper)
else:
    print(scissors)
