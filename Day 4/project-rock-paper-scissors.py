import random

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

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of ASCII art for display
ascii_list = [rock, paper, scissor]

# List of choices for logic
choices = ["rock", "paper", "scissor"]

# Get user's choice
user_choice = input("Pick one from rock, paper and scissor: ").lower()

# Check if valid input
if user_choice not in choices:
    print("Invalid input. Choose rock, paper or scissor.")
else:
    user_index = choices.index(user_choice)
    user_pick = ascii_list[user_index]

    comp_index = random.randint(0, 2)
    comp_pick = ascii_list[comp_index]

    print(f"\nYou picked:\n{user_pick}")
    print(f"Computer picked:\n{comp_pick}")

    # Game logic
    if user_index == comp_index:
        print("It's a draw!")
    elif (user_index == 0 and comp_index == 2) or \
         (user_index == 1 and comp_index == 0) or \
         (user_index == 2 and comp_index == 1):
        print("You win!")
    else:
        print("You lose!")
