#number guessing game
#if user pick hard , only 5 attempt, if user pick easy only 10 attempt
import random

from art import logo
print(logo)

guessed_number=random.randint(1,100)
print(f"i am thinking the number between 1 and 100 {guessed_number}" )

difficulty_choice=input("do you want easy or hard? press e or h : ").lower()

def logic(guess):
    
    user_number=int(input("what is the guessed number?: "))
    if guess>user_number:
        print("too low")
    elif guess<user_number:
        print("too high")
    else:
        print(f"its right number, guessed number was {guess}")
        exit()

count=10           
if difficulty_choice=="e":
    for i in range(0,10):
        logic(guessed_number)
        count-=1
        print(f"you have {count} attempt left")
        print(f"you lost the game, guessed number was {guessed_number}") 

count=5
if difficulty_choice=="h":
    for i in range(0,5):
        logic(guessed_number)
        count-=1
        print(f"you have {count} attempt left")
    if count==0:
       print(f"you lost the game, guessed number was {guessed_number}") 