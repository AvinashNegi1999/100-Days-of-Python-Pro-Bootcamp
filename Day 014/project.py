import random  # To randomly select items from the data
from art import logo  # ASCII art logo to show at the start of the game
from game import data  # List of celebrity dictionaries

print(logo)  # Display the logo

score = 0  # Initialize score counter
should_continue = True  # Flag to control the game loop

# Select two different random celebrity entries from the data
a_guess = random.choice(data)
b_guess = random.choice(data)

while should_continue:
    A = a_guess['follower_count']  # Follower count of option A
    B = b_guess['follower_count']  # Follower count of option B
    
    # Display information about both celebrities
    print(f"\nCompare A: {a_guess['name']}, a {a_guess['description']} from {a_guess['country']}")
    print("VS")
    print(f"Against B: {b_guess['name']}, a {b_guess['description']} from {b_guess['country']}")
    
    # Ask user to guess who has more followers
    guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

    # Check if user's guess is correct
    if (A > B and guess == "A") or (B > A and guess == "B"):
        score += 1  # Increase score for correct guess
        print(f"Correct! Current score: {score}")
        a_guess = b_guess  # B becomes the new A
        b_guess = random.choice(data)  # Pick a new B

        # Ensure B is not the same as A
        while b_guess == a_guess:
            b_guess = random.choice(data)  # Keep picking until different
    else:
        # If the guess is wrong, end the game
        print(f"Wrong! Final score: {score}")
        print(f"A had {A}M followers, B had {B}M followers.")
        should_continue = False  # Exit the loop
