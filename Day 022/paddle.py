from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")              # * Makes the paddle a square shape
        self.color("cyan")                # * Paddle color is cyan
        self.shapesize(stretch_wid=5, stretch_len=1)  # * Makes the square tall like a paddle
        self.penup()                     # * So it doesn't draw a line when moving
        self.goto(position)              # * Starts the paddle at the given position

    def go_up(self):
        # * Only move up if the paddle is not too close to the top of the screen
        if self.ycor() < 250:
            new_y = self.ycor() + 20     # * Move up by 20 units
            self.goto(self.xcor(), new_y)  # * Set the new position

    def go_down(self):
        # * Only move down if the paddle is not too close to the bottom of the screen
        if self.ycor() > -230:
            new_y = self.ycor() - 20     # * Move down by 20 units
            self.goto(self.xcor(), new_y)  # * Set the new position
