# ! Import the Turtle class from the turtle module
from turtle import Turtle

# * Create a Scoreboard class that inherits from Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()              # ! Call the Turtle class constructor
        self.color("white")             # * Set the color of the text
        self.penup()                   # * Prevent drawing lines
        self.hideturtle()              # * Hide the turtle icon (we just want text)
        self.l_score = 0               # * Left player score starts at 0
        self.r_score = 0               # * Right player score starts at 0
        self.update_scoreboard()       # * Draw the initial score

    # * This function draws or updates the score text on the screen
    def update_scoreboard(self):
        self.clear()                   # * Clear the old score before writing a new one

        # * Show the left score on the left side of the screen
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Times New Roman", 80, "normal"))

        # * Show the right score on the right side of the screen
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Times New Roman", 80, "normal"))

    # * This function is called when the left player scores a point
    def l_point(self):
        self.l_score += 1              # * Add 1 to left player's score
        self.update_scoreboard()       # * Refresh the scoreboard display

    # * This function is called when the right player scores a point
    def r_point(self):
        self.r_score += 1              # * Add 1 to right player's score
        self.update_scoreboard()       # * Refresh the scoreboard display
