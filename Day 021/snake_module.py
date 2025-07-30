from turtle import Turtle

# --- Constants for snake settings ---
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Initial snake body segments
MOVE_DISTANCE = 20                                # Distance moved per step
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    '''A class to create and control the snake in the game.'''

    def __init__(self):
        '''Initialize the snake body and set the head.'''
        self.segments = []              # List to store all segments
        self.create_snake()            # Create initial snake
        self.head = self.segments[0]   # Set the first segment as the head

    def create_snake(self):
        '''Create initial snake body using STARTING_POSITION list.'''
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        '''Add a new segment to the snake at the given position.'''
        new_segment = Turtle("square")   # Use square shape for each segment
        new_segment.color("white")       # Snake color
        new_segment.penup()              # Prevent drawing lines
        new_segment.goto(position)       # Move to position
        self.segments.append(new_segment)

    def extend(self):
        '''Extend the snake by adding a new segment to the tail.'''
        self.add_segment(self.segments[-1].position())

    def move(self):
        '''Move the snake forward by shifting each segment to the one before it.'''
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move head forward

    def up(self):
        '''Change direction to up, unless already going down.'''
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        '''Change direction to down, unless already going up.'''
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        '''Change direction to left, unless already going right.'''
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        '''Change direction to right, unless already going left.'''
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
