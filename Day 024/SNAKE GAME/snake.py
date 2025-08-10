from turtle import Turtle

# ------------------- Constants -------------------
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial 3-segment positions
MOVE_DISTANCE = 20                                # Distance moved per step
UP = 90                                           # Angle for upward movement
DOWN = 270                                        # Angle for downward movement
LEFT = 180                                        # Angle for left movement
RIGHT = 0                                         # Angle for right movement


class Snake:

    def __init__(self):
        self.segments = []            # List to hold all snake body segments
        self.create_snake()           # Create initial snake body
        self.head = self.segments[0]  # First segment is the snake's head

    def create_snake(self):
        """Create the snake at the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a single new segment to the snake."""
        new_segment = Turtle("square")  # Create a square-shaped turtle segment
        new_segment.color("white")      # Set segment color
        new_segment.penup()             # Prevent drawing lines while moving
        new_segment.goto(position)      # Place segment at given position
        self.segments.append(new_segment)  # Add to list of segments

    def extend(self):
        """Add a new segment to the snake's tail."""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        """Reset the snake after collision."""
        # Move existing segments off-screen (so they disappear instantly)
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()     # Remove all segments from list
        self.create_snake()       # Create a fresh snake
        self.head = self.segments[0]

    def move(self):
        """Move the snake forward by shifting segments."""
        # Move each segment to the position of the one in front of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward

    def up(self):
        """Change direction to UP unless going DOWN."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change direction to DOWN unless going UP."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change direction to LEFT unless going RIGHT."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change direction to RIGHT unless going LEFT."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
