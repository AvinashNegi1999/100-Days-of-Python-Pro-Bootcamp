from turtle import Turtle

# Constants for text alignment and font style
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'bold')


class Scoreboard(Turtle):
    '''A class to manage the scoreboard in the turtle game.'''

    def __init__(self):
        '''Initialize the scoreboard with score = 0 and position it on screen.'''
        super().__init__()
        self.score = 0
        self.hideturtle()        # Hide the turtle cursor
        self.penup()             # Prevent drawing while moving
        self.color("cyan")       # Set scoreboard font color
        self.goto(0, 260)        # Move to top-center of the screen

    def start_scoreboard(self):
        '''Display the initial score on the screen.'''
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_scoreboard(self):
        '''Increase the score by 1 and update the scoreboard.'''
        self.clear()             # Clear previous score
        self.score += 1          # Increment score
        self.start_scoreboard()  # Re-write updated score

    def game_over(self):
        '''Display GAME OVER message in the center of the screen.'''
        self.goto(0, 0)          # Move to screen center
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
