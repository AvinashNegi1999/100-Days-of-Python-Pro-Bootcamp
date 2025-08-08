"""
Turtle Crossing Game - Main File
--------------------------------
This script runs the main game loop for the Turtle Crossing game.
The player controls a turtle, avoiding cars while trying to cross
to the other side. Points are awarded for each successful crossing.

Author: Avinash Negi
Date: August 8, 2025
"""

# ==============================
# IMPORTS
# ==============================
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


# ==============================
# SCREEN SETUP
# ==============================
screen = Screen()
screen.setup(width=600, height=600)  # Set screen size
screen.title("Turtle Crossing")  # Set game title
screen.tracer(0)  # Turn off auto animation for manual updates


# ==============================
# GAME OBJECTS
# ==============================
player = Player()         # The player-controlled turtle
scoreboard = Scoreboard() # Displays score and messages
car_manager = CarManager() # Handles car creation and movement


# ==============================
# EVENT LISTENERS
# ==============================
screen.listen()
screen.onkeypress(player.move_up, "Up")  # Move turtle when "Up" key is pressed


# ==============================
# GAME LOOP
# ==============================
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Delay to control game speed
    screen.update()  # Refresh the screen

    # Create new cars and move existing ones
    car_manager.add_car()
    car_manager.move_car()

    # Check if player reached the top
    if player.ycor() > 310:
        scoreboard.player_point()       # Increase score
        player.starting_position()      # Reset player to start
        car_manager.increase_speed()    # Make cars faster

    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:   # Collision detected
            game_is_on = False
            scoreboard.game_over()      # Display game over message


# ==============================
# EXIT ON CLICK
# ==============================
screen.exitonclick()
