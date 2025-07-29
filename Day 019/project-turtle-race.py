# 🐢 Turtle Race Game Setup
# Q: Write a Python program using the turtle module to:
#    - Create 7 turtles with rainbow colors
#    - Ask the user to bet on which turtle will win the race
#    - Position all turtles at the left side of the screen
#    - (Optional) You can later add movement logic for the race
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color:"
)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
y_positions = [-100, -70, -40, -10, 20, 50, 80]
all_turtles = []

for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-220, y=y_positions[i])
    all_turtles.append(new_turtle)

# Start race only if user placed a bet
if user_bet:
    race_on = True
    while race_on:
        for turtle in all_turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)

            if turtle.xcor() > 230:
                race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet.lower():
                    print(f"You've won! The {winning_color} turtle is the winner! 🏆")
                else:
                    print(f"You lost! The {winning_color} turtle won the race.")

screen.exitonclick()
