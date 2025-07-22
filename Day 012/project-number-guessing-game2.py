import random  # To generate random number

from art import logo
print(logo)
print(" Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)  # Random number between 1 and 100
attempts = 10 if input("Choose difficulty (e/h): ").lower() == 'e' else 5  # Easy = 10 tries, Hard = 5

while attempts > 0:
    guess = int(input("Make a guess: "))  # User inputs guess
    if guess == number:
        print(f" Correct! The number was {number}.")  # Win message
        break
    elif guess < number:
        print(" Too low.")  # Hint if guess is low
    else:
        print(" Too high.")  # Hint if guess is high
    
    attempts -= 1  # Decrease attempts
    print(f"Attempts left: {attempts}")  # Show remaining attempts
else:
    print(f" You lose. The number was {number}.")  # Loss message if all attempts used
