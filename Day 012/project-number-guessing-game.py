import random  # To use random number generation
from art import logo  # Importing logo from art.py

print(logo)

secret_number = random.randint(1, 100)  # Random number between 1 and 100
print(f"I am thinking of a number between 1 and 100: {secret_number}")  # Debug print, remove in final version

difficulty = input("Choose difficulty level - Easy (e) or Hard (h): ").lower()  # Get user difficulty choice

def check_user_guess(target_number):  # Function to check the user's guess
    user_guess = int(input("Enter your guess: "))  # Take guess input
    if target_number > user_guess:
        print("Too low")  # Hint if guess is less than target
    elif target_number < user_guess:
        print("Too high")  # Hint if guess is more than target
    else:
        print(f"Correct! The number was {target_number}")  # Correct guess message
        exit()  # Exit program on correct guess

attempts_remaining = 10  # Default attempts for easy mode
if difficulty == "e":
    for _ in range(10):  # Loop for 10 attempts
        check_user_guess(secret_number)
        attempts_remaining -= 1  # Reduce attempts
        print(f"You have {attempts_remaining} attempts left")  # Show remaining attempts
        print(f"You lost the game. The correct number was {secret_number}")  # This should be outside loop ideally

attempts_remaining = 5  # Attempts for hard mode
if difficulty == "h":
    for _ in range(5):  # Loop for 5 attempts
        check_user_guess(secret_number)
        attempts_remaining -= 1
        print(f"You have {attempts_remaining} attempts left")
    if attempts_remaining == 0:
        print(f"You lost the game. The correct number was {secret_number}")  # Final loss message
