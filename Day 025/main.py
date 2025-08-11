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
#    - If 'Exit': save missing states to CSV & break.
#    - If valid guess: add to guessed list, get coordinates, and write name on map.
# 7. Keep window open after game ends.
# ------------------------------------------------------------


import turtle
import pandas

# ----------------------- Screen Setup -----------------------
# Create a window for the game
screen = turtle.Screen()
screen.title("U.S. States Game")

# Load the map image as turtle shape
image = "C:/Users/avina/OneDrive/Documents/GitHub/100-Days-of-Python-Code-challenge/Day 025/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# ----------------------- Data Setup -----------------------
# Read CSV containing states and their coordinates
data = pandas.read_csv("C:/Users/avina/OneDrive/Documents/GitHub/100-Days-of-Python-Code-challenge/Day 025/50_states.csv")

# Convert state column to a list
all_states = data.state.to_list()

# Keep track of guessed states
guessed_states = []

# ----------------------- Main Game Loop -----------------------
while len(guessed_states) < 50:
    # Ask the user to guess a state name
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    ).title()  # Capitalize first letter for uniform matching

    # If player types 'Exit', save the states they missed
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        pandas.DataFrame(missing_states).to_csv("states_to_learn.csv")
        break

    # If guessed state is correct and not already guessed
    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        # Get coordinates of the guessed state
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)

        # Create a turtle to write the state name at its location
        marker = turtle.Turtle()
        marker.hideturtle()  # Hide the turtle icon
        marker.penup()       # Lift pen to move without drawing
        marker.goto(x, y)    # Go to the state's coordinates
        marker.write(answer_state)  # Write the state's name
