# ! Import necessary classes and modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# * Create the game screen
screen = Screen()
screen.bgcolor("#0a0a23")            # * Set background color to black
screen.setup(width=800, height=600)  # * Set screen size
screen.title("Pong Game")            # * Title of the window
screen.tracer(0)                     # * Turn off automatic screen updates (we will update it manually)

# * Create right and left paddles at specific positions
right_paddle = Paddle((350, 0))      # * Right paddle on the right side of screen
left_paddle = Paddle((-350, 0))      # * Left paddle on the left side

# * Create the ball
ball = Ball()

# * Create the scoreboard
scoreboard = Scoreboard()

# * Listen for key presses
screen.listen()

# * Control right paddle using arrow keys
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")

# * Control left paddle using W and S keys
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

# TODO: Start the game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)       # * Control ball speed
    screen.update()                   # * Refresh the screen
    ball.move()                      # * Move the ball

    # * Make the ball bounce off top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # * Make the ball bounce off paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or \
       (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # ! Right player misses, left player scores
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # ! Left player misses, right player scores
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

# * Exit the game when user clicks on screen
screen.exitonclick()
