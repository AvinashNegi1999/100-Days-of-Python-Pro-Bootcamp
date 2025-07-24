import random
from art import logo
from game import data

print(logo)

score = 0
should_continue = True

a_guess = random.choice(data)
b_guess = random.choice(data)

while should_continue:
    A = a_guess['follower_count']
    B = b_guess['follower_count']
    
    print(f"\nCompare A: {a_guess['name']}, a {a_guess['description']} from {a_guess['country']}")
    print("VS")
    print(f"Against B: {b_guess['name']}, a {b_guess['description']} from {b_guess['country']}")
    
    guess = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

    if (A > B and guess == "A") or (B > A and guess == "B"):
        score += 1
        print(f"Correct! Current score: {score}")
        a_guess = b_guess
        b_guess = random.choice(data)
        while b_guess == a_guess:
            b_guess = random.choice(data)  # avoid same comparison
    else:
        print(f"Wrong! Final score: {score}")
        print(f"A had {A}M followers, B had {B}M followers.")
        should_continue = False
