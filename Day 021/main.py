from turtle import Screen
from snake_module import Snake
from food import Food
from scoreboard import Scoreboard
import time

# --- Setup Screen ---
screen = Screen()
screen.setup(width=600, height=600)     # Define screen size
screen.bgcolor("gray")                 # Set background color
screen.title("Snake Game")              # Set window title
screen.tracer(0)                        # Turn off auto-refresh for manual control

# --- Create Game Objects ---
snake = Snake()                         # Initialize the snake
food = Food()                           # Initialize the food
scoreboard = Scoreboard()               # Initialize the scoreboard

# --- Listen to Keyboard Inputs ---
screen.listen()
screen.onkey(snake.up, "Up")            # Bind arrow keys to snake movement
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
scoreboard.start_scoreboard()           # Display starting score

# --- Main Game Loop ---
game_is_on = True
while game_is_on:
    screen.update()                     # Refresh screen manually
    time.sleep(0.1)                     # Control game speed
    snake.move()                        # Move the snake forward

    # --- Detect Collision with Food ---
    if snake.head.distance(food) < 15:
        scoreboard.increase_scoreboard()  # Increase score
        snake.extend()                    # Grow the snake
        food.refresh()                    # Move food to new position

    # --- Detect Collision with Wall ---
    if (
        snake.head.xcor() > 280 or
        snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or
        snake.head.ycor() < -280
    ):
        game_is_on = False
        scoreboard.game_over()           # Display Game Over

    # --- Detect Collision with Tail ---
    for segment in snake.segments[1:]:  # Ignore the head
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()       # Game ends on tail collision

# --- Exit on Click ---
screen.exitonclick()
