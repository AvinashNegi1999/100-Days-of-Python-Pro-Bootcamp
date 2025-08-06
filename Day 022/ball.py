# Import the Turtle class from the turtle module
from turtle import Turtle

# Create a Ball class that inherits from Turtle
class Ball(Turtle):

    def __init__(self):
        super().__init__()                # Call the Turtle's constructor
        self.shape("square")             # Set the shape of the ball
        self.color("yellow")              # Set the color of the ball
        self.penup()                     # Don't draw lines when the ball moves
        self.x_move = 10                 # How much the ball moves in the x direction
        self.y_move = 10                 # How much the ball moves in the y direction
        self.move_speed = 0.1            # Initial speed of the ball (used for delay)

    # Move the ball by updating its x and y coordinates
    def move(self):
        new_x = self.xcor() + self.x_move   # Current x position + step size
        new_y = self.ycor() + self.y_move   # Current y position + step size
        self.goto(new_x, new_y)             # Move the ball to the new position

    # Bounce the ball off top and bottom walls (reverse y direction)
    def bounce_y(self):
        self.y_move *= -1                   # Change direction (up becomes down or vice versa)
        self.move_speed *= 0.9              # Increase speed slightly (lower delay)

    # Bounce the ball off paddles (reverse x direction)
    def bounce_x(self):
        self.x_move *= -1                   # Change horizontal direction
        self.move_speed *= 0.9              # Increase speed slightly

    # Reset the ball to the center and change its direction
    def reset_position(self):
        self.home()                         # Move the ball back to the center (0,0)
        self.move_speed = 0.1               # Reset speed to normal
        self.bounce_x()                     # Change direction to keep game going
