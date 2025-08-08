"""
Player Module
-------------
This module defines the Player class for the Turtle Crossing game.
The player is represented as a turtle that can move upward and 
resets to the starting position after reaching the finish line.

Author: Avinash Negi
Date: August 8, 2025
"""

from turtle import Turtle

# ==============================
# CONSTANTS
# ==============================
STARTING_POSITION = (0, -280)  # Starting coordinates for the player
MOVE_DISTANCE = 10             # Distance the player moves each step
FINISH_LINE_Y = 280             # Y-coordinate for the finish line


# ==============================
# PLAYER CLASS
# ==============================
class Player(Turtle):
    """
    Represents the player in the Turtle Crossing game.
    The player can move upward and reset to the starting position.
    """

    # ------------------------------
    # INITIALIZATION
    # ------------------------------
    def __init__(self):
        """
        Initialize the player turtle with shape, color, and starting position.
        """
        super().__init__()
        self.setheading(90)               # Face upward
        self.shape("turtle")               # Turtle shape
        self.color("black")                # Player color
        self.penup()                       # Prevent drawing lines
        self.goto(STARTING_POSITION)       # Move to starting position

    # ------------------------------
    # MOVEMENT
    # ------------------------------
    def move_up(self):
        """
        Move the player upward by MOVE_DISTANCE.
        """
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # ------------------------------
    # RESET POSITION
    # ------------------------------
    def starting_position(self):
        """
        Reset the player to the starting position.
        """
        self.goto(STARTING_POSITION)
