"""
Scoreboard Module
-----------------
This module defines the Scoreboard class for the Turtle Crossing game.
The scoreboard displays the player's current level and shows a 
'Game Over' message when the game ends.

Author: Avinash Negi
Date: August 8, 2025
"""

from turtle import Turtle

# ==============================
# CONSTANTS
# ==============================
ALIGNMENT = 'left'                       # Text alignment for scoreboard
FONT = ("Courier", 24, "normal")          # Font style for text


# ==============================
# SCOREBOARD CLASS
# ==============================
class Scoreboard(Turtle):
    """
    Displays and manages the scoreboard for the Turtle Crossing game.
    """

    # ------------------------------
    # INITIALIZATION
    # ------------------------------
    def __init__(self):
        """
        Initialize the scoreboard with starting level and position.
        """
        super().__init__()
        self.color("black")               # Scoreboard text color
        self.penup()                       # Prevent drawing lines
        self.hideturtle()                  # Hide turtle cursor
        self.goto(-290, 260)               # Position at top-left corner
        self.player_score = 0              # Starting level
        self.update_scoreboard()            # Display initial score

    # ------------------------------
    # UPDATE DISPLAY
    # ------------------------------
    def update_scoreboard(self):
        """
        Clear and redraw the scoreboard with the current level.
        """
        self.clear()
        self.write(f"Level: {self.player_score}", align=ALIGNMENT, font=FONT)

    # ------------------------------
    # INCREASE SCORE
    # ------------------------------
    def player_point(self):
        """
        Increase the player's score by 1 and update the display.
        """
        self.player_score += 1
        self.update_scoreboard()

    # ------------------------------
    # GAME OVER MESSAGE
    # ------------------------------
    def game_over(self):
        """
        Display the 'GAME OVER' message at the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
