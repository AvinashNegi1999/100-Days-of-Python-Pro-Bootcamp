from turtle import Turtle

# ------------------- Constants -------------------
ALIGNMENT = "center"                     # Text alignment for scoreboard display
FONT = ("Courier", 24, "normal")          # Font style for scoreboard text

# Absolute path to data file (no os module, forward slashes to avoid escape issues)
DATA_FILE_PATH = "C:/Users/avina/OneDrive/Documents/GitHub/100-Days-of-Python-Code-challenge/Day 024/SNAKE GAME/data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        """Initialize scoreboard with default settings."""
        super().__init__()                # Initialize Turtle as base class
        self.score = 0                    # Current game score
        self.high_score = 0               # Highest score saved in file
        self.color("white")               # Set text color
        self.penup()                      # Avoid drawing lines when moving
        self.goto(0, 260)                  # Position scoreboard at top center
        self.hideturtle()                  # Hide turtle cursor
        self.update_scoreboard()           # Display initial score

    def update_scoreboard(self):
        """Clear and rewrite the scoreboard display."""
        self.clear()                       # Clear previous text
        self.read_file()                   # Load high score from file
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT, font=FONT
        )

    def reset(self):
        """Reset score and update high score if needed."""
        if self.score > self.high_score:   # If current score beats high score
            self.high_score = self.score
            self.write_file()
        self.score = 0                     # Reset current score to 0
        self.update_scoreboard()           # Refresh scoreboard

    def increase_score(self):
        """Increase the score by 1 and update the display."""
        self.score += 1
        self.update_scoreboard()

    def read_file(self):
        """Read high score from a file."""
        with open(DATA_FILE_PATH) as file:
            self.high_score = int(file.read())

    def write_file(self):
        """Write the high score to a file."""
        with open(DATA_FILE_PATH, mode="w") as file:
            file.write(f"{self.high_score}")
