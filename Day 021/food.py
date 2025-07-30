from turtle import Turtle
import random

class Food(Turtle):
    '''A class to create and manage the food object in the snake game.'''

    def __init__(self):
        '''Initialize the food with shape, size, color, and place it randomly on the screen.'''
        super().__init__()
        self.shape("circle")                         # Food shape is a circle
        self.penup()                                 # No drawing when food moves
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make it smaller (default size is too big)
        self.color("red")                            # Food color (can be changed for variety)
        self.speed("fastest")                        # Instantly moves when relocated
        self.refresh()                               # Place food at random position

    def refresh(self):
        '''Move the food to a new random location within screen bounds.'''
        random_x = random.randint(-280, 280)         # X coordinate within screen width
        random_y = random.randint(-280, 280)         # Y coordinate within screen height
        self.goto(random_x, random_y)                # Move food to the new random location
