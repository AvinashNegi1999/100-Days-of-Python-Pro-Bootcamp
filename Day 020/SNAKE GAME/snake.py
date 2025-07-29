from turtle import Turtle

# Constants for snake setup and movement
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Snake starts with 3 segments
MOVE_DISTANCE = 20

# Direction angles
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        # List to hold all snake segments
        self.segments = []

        # Create the initial snake body
        self.create_snake()

        # Set the first segment as the head of the snake
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake with 3 square segments."""
        for position in STARTING_POSITION:
            new_segment = Turtle("square")  # Create square turtle
            new_segment.color("white")      # Set color to white
            new_segment.penup()             # Don't draw lines while moving
            new_segment.goto(position)      # Move segment to starting position
            self.segments.append(new_segment)  # Add segment to the list

    def move(self):
        """Move the snake forward by moving each segment to the position of the one ahead of it."""
        # Move each segment to the previous segment's position, starting from the tail
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # Move the head forward
        self.head.forward(MOVE_DISTANCE)

    # Movement direction methods (prevent going directly backwards)
    def up(self):
        """Change direction to UP if not currently going DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to DOWN if not currently going UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to LEFT if not currently going RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to RIGHT if not currently going LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
