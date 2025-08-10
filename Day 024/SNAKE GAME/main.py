from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# ------------------- Screen Setup -------------------
screen = Screen()
screen.setup(width=600, height=600)   # Set window size
screen.bgcolor("black")               # Set background color
screen.title("My Snake Game")         # Window title
screen.tracer(0)                      # Turn off automatic screen updates (manual control)

# ------------------- Game Objects -------------------
snake = Snake()                        # Create Snake object
food = Food()                          # Create Food object
scoreboard = Scoreboard()              # Create Scoreboard object

# ------------------- Controls -------------------
screen.listen()                        # Listen for keyboard input
screen.onkey(snake.up, "Up")           # Move up on UP arrow key
screen.onkey(snake.down, "Down")       # Move down on DOWN arrow key
screen.onkey(snake.left, "Left")       # Move left on LEFT arrow key
screen.onkey(snake.right, "Right")     # Move right on RIGHT arrow key

# ------------------- Game Loop -------------------
game_is_on = True
while game_is_on:
    screen.update()                    # Refresh the screen manually
    time.sleep(0.1)                     # Delay to control game speed
    snake.move()                        # Move the snake forward

    # --- Detect collision with food ---
    if snake.head.distance(food) < 15:  # If head is close to food
        food.refresh()                  # Move food to a new random position
        snake.extend()                  # Add new segment to snake
        scoreboard.increase_score()     # Update score

    # --- Detect collision with wall ---
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280):
        scoreboard.reset()              # Reset score
        snake.reset()                   # Reset snake to starting position

    # --- Detect collision with tail ---
    for segment in snake.segments:
        if segment == snake.head:       # Skip checking head against itself
            continue
        if snake.head.distance(segment) < 10:  # If head touches any segment
            snake.reset()               # Reset snake to starting position

# Exit when screen is clicked
screen.exitonclick()
