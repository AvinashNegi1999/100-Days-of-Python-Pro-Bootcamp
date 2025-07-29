from turtle import Screen
from snake import Snake
import time

# --------------------- Screen Setup ---------------------
screen = Screen()
screen.setup(width=600, height=600)   # Set window size
screen.bgcolor("black")               # Set background color
screen.title("Snake Game")            # Set window title
screen.tracer(0)                      # Turn off automatic screen updates

# --------------------- Create Snake ---------------------
snake = Snake()

# --------------------- Keyboard Controls ---------------------
screen.listen()                       # Listen for keyboard input
screen.onkey(snake.up, "Up")          # Move up when "Up" arrow is pressed
screen.onkey(snake.down, "Down")      # Move down when "Down" arrow is pressed
screen.onkey(snake.left, "Left")      # Move left when "Left" arrow is pressed
screen.onkey(snake.right, "Right")    # Move right when "Right" arrow is pressed

# --------------------- Game Loop ---------------------
game_is_on = True
while game_is_on:
    screen.update()       # Update the screen manually (since tracer is off)
    time.sleep(0.1)       # Delay to control snake speed
    snake.move()          # Move the snake forward

# --------------------- Exit on Click ---------------------
screen.exitonclick()
