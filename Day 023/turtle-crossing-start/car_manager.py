from turtle import Turtle
import random

# List of possible car colors
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Initial speed of the cars (in pixels per move)
STARTING_MOVE_DISTANCE = 5

# How much the speed increases each level
MOVE_INCREMENT = 10


class CarManager:
    """
    Class to manage the creation, movement, and speed of cars in the Turtle Crossing game.
    """

    def __init__(self):
        """
        Initializes the CarManager with an empty car list and sets the starting speed.
        """
        self.cars = []  # List to store all car objects
        self.starting_speed = STARTING_MOVE_DISTANCE  # Initial speed of cars
        self.increment = MOVE_INCREMENT  # Speed increase per level

    def add_car(self):
        """
        Randomly creates and adds a new car to the game.

        Cars only spawn with a 1/6 probability each time this function is called.
        Each car:
        - Has a rectangular shape (2 units long, 1 unit wide)
        - Has a random color from COLORS
        - Starts on the right side of the screen at a random vertical position
        """
        car_chance = random.randint(1, 6)  # 1 in 6 chance to create a car
        if car_chance == 6:
            new_car = Turtle("square")  # Create car body
            new_car.penup()  # Prevent drawing lines
            new_car.color(random.choice(COLORS))  # Random color
            new_car.shapesize(stretch_len=2, stretch_wid=1)  # Make it look like a car
            random_y = random.randint(-250, 250)  # Random lane position
            new_car.goto(300, random_y)  # Start just off-screen on the right
            self.cars.append(new_car)  # Add to car list

    def increase_speed(self):
        """
        Increases the speed of all cars.

        Called each time the player advances to the next level.
        """
        self.starting_speed += self.increment

    def move_car(self):
        """
        Moves all cars from right to left at the current speed.
        """
        for car in self.cars:
            car.backward(self.starting_speed)
