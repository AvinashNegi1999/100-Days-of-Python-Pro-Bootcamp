# Import the random module so the computer can make a random choice
import random

# Define the ASCII art for each option to make the game more fun and visual
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
---'    ____)____
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

# Create a list of ASCII art in the same order as the options
ascii_art = [rock, paper, scissors]

# List of valid choices in the game
options = ["rock", "paper", "scissors"]

# Ask the user to enter their choice and convert it to lowercase
user_input = input("Pick one from Rock, Paper, or Scissors: ").lower()

# Check if the user's input is valid
if user_input not in options:
    print("Invalid input. Please choose either rock, paper, or scissors.")
else:
    # Get the index of the user's choice
    user_index = options.index(user_input)
    # Get the corresponding ASCII art
    user_choice_art = ascii_art[user_index]

    # Generate a random choice for the computer (0, 1, or 2)
    computer_index = random.randint(0, 2)
    computer_choice_art = ascii_art[computer_index]
    computer_input = options[computer_index]

    # Display both choices
    print(f"\nYou chose: {user_input.capitalize()}")
    print(user_choice_art)
    print(f"Computer chose: {computer_input.capitalize()}")
    print(computer_choice_art)

    # Compare choices to determine the result
    if user_index == computer_index:
        print("It's a draw! You both chose the same.")
    
    # Case: User chose Rock
    elif user_index == 0 and computer_index == 2:
        print("Rock crushes Scissors!")
        print("You win!")
    
    # Case: User chose Paper
    elif user_index == 1 and computer_index == 0:
        print("Paper covers Rock!")
        print("You win!")

    # Case: User chose Scissors
    elif user_index == 2 and computer_index == 1:
        print("Scissors cut Paper!")
        print("You win!")

    # If none of the winning cases match, user loses
    else:
        if user_index == 0 and computer_index == 1:
            print("Paper covers Rock!")
        elif user_index == 1 and computer_index == 2:
            print("Scissors cut Paper!")
        elif user_index == 2 and computer_index == 0:
            print("Rock crushes Scissors!")
        print("You lose! Better luck next time.")
