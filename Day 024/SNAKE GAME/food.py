from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        """Initialize the food object for the Snake game."""
        super().__init__()                        # Initialize Turtle base class
        self.shape("circle")                       # Shape of the food
        self.penup()                                # Prevent drawing when moving
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make it smaller than default
        self.color("blue")                          # Food color
        self.speed("fastest")                       # Instantly appear without animation
        self.refresh()                              # Place food at a random position

    def refresh(self):
        """Move the food to a new random location on the screen."""
        # Choose random coordinates within the screen bounds
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)               # Move food to the new position
