# ------------------------------------------------------------
# U.S. States Game — Steps
# ------------------------------------------------------------
# 1. Ensure map image (blank_states_img.gif) & CSV (50_states.csv) exist with correct paths.
# 2. Import turtle (GUI) & pandas (CSV handling).
# 3. Create game window & set title.
# 4. Load map image as turtle shape.
# 5. Read CSV, get list of all states, and make guessed_states list.
# 6. Loop until 50 states guessed or player exits:
#    - Ask for state name (show score in title).
#    - If 'Exit': save missing states to CSV in script folder & break.
#    - If valid guess: add to guessed list, get coordinates, and write name on map.
# 7. Keep window open after game ends.
# ------------------------------------------------------------

import turtle
import pandas
import os

# ----------------------- Screen Setup -----------------------
# Create a turtle screen window and set its title
screen = turtle.Screen()
screen.title("U.S. States Game")

# Define the path to the U.S. map image and add it as a turtle shape
image = "C:/Users/avina/OneDrive/Documents/GitHub/100-Days-of-Python-Code-challenge/Day 025/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)  # Set the turtle shape to the map image

# ----------------------- Data Setup -----------------------
# Read the CSV file containing the list of states and their coordinates
data = pandas.read_csv("C:/Users/avina/OneDrive/Documents/GitHub/100-Days-of-Python-Code-challenge/Day 025/50_states.csv")

# Extract the list of all state names for validation
all_states = data.state.to_list()

# Initialize an empty list to keep track of states guessed by the user
guessed_states = []

# Get the directory where this Python script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the full path to save the missing states CSV file in the same folder
output_path = os.path.join(script_dir, "states_to_learn.csv")

# ----------------------- Main Game Loop -----------------------
# Run the game loop until the user has guessed all 50 states
while len(guessed_states) < 50:
    # Prompt the user to input a state name, showing current score in the title bar
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    # Proceed only if the user provided some input (not cancelled)
    if answer_state:
        # Normalize input by capitalizing first letters to match CSV format
        answer_state = answer_state.title()

        # If user types 'Exit', save missing states and end the game
        if answer_state == "Exit":
            # Create a list of states not yet guessed
            missing_states = [state for state in all_states if state not in guessed_states]
            # Save missing states to CSV file in the script directory
            pandas.DataFrame(missing_states).to_csv(output_path)
            break  # Exit the loop and end the game

        # If the guessed state is correct and hasn't been guessed before
        if answer_state in all_states and answer_state not in guessed_states:
            # Add the state to the guessed list
            guessed_states.append(answer_state)

            # Get the x, y coordinates of the guessed state from the CSV data
            state_data = data[data.state == answer_state]
            x = int(state_data.x)
            y = int(state_data.y)

            # Create a turtle to write the state name on the map
            marker = turtle.Turtle()
            marker.hideturtle()   # Hide the turtle cursor
            marker.penup()        # Lift the pen to move without drawing lines
            marker.goto(x, y)     # Move the turtle to the state's coordinates
            marker.write(answer_state)  # Write the state name on the map

# Keep the turtle graphics window open after the game ends
screen.mainloop()
