"""
====================================================
FLASHY FLASHCARD APP
====================================================
Author  : Avinash Negi
Project : Day 31 - 100 Days of Python Challenge
Purpose : A flashcard app to learn French–English words.
Features:
    ✅ Randomly shows French words
    ✅ Flips card after 3 seconds to show English translation
    ✅ Tracks learned words and saves progress in CSV
    ✅ Provides ✓ (known) and ✗ (unknown) buttons
====================================================
"""

# * ---------------- IMPORTS ---------------- *
from tkinter import *
import pandas as pd
import random
import os

# * ---------------- CONSTANTS ---------------- *
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

# ✅ Define paths (relative so project can be zipped & shared easily)
DATA_PATH = r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 031\data"
IMAGE_PATH = r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 031\images"


# * ---------------- DATA HANDLING ---------------- *
try:
    # ✅ Load saved progress if available
    data = pd.read_csv(os.path.join(DATA_PATH, "words_to_learn.csv"))
except FileNotFoundError:
    # ! If no progress file, load original dataset
    original_data = pd.read_csv(os.path.join(DATA_PATH, "french_words.csv"))
    to_learn = original_data.to_dict(orient="records")
else:
    # ✅ Convert loaded CSV into list of dicts
    to_learn = data.to_dict(orient="records")


# * ---------------- FUNCTIONS ---------------- *
def next_card():
    """
    ✅ Picks a new random French word and updates the card.
    ✅ Resets the flip timer for each new card.
    """
    global current_card, flip_timer
    try:
        window.after_cancel(flip_timer)  # ✅ Cancel previous flip timer
    except:
        pass
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)  # ✅ Auto-flip after 3 seconds


def flip_card():
    """
    ✅ Flips the card to show the English translation.
    """
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)


def is_known():
    """
    ✅ Removes the current word from learning list if known.
    ✅ Saves progress into 'words_to_learn.csv'.
    """
    if current_card in to_learn:
        to_learn.remove(current_card)
        pd.DataFrame(to_learn).to_csv(
            os.path.join(DATA_PATH, "words_to_learn.csv"), index=False
        )
    next_card()


# * ---------------- UI SETUP ---------------- *
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ✅ Flip timer for automatic card flip
flip_timer = window.after(3000, func=flip_card)

# ✅ Create the flashcard canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file=os.path.join(IMAGE_PATH, "card_front.png"))
card_back_img = PhotoImage(file=os.path.join(IMAGE_PATH, "card_back.png"))
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ✅ Buttons for "Wrong" and "Right"
cross_image = PhotoImage(file=os.path.join(IMAGE_PATH, "wrong.png"))
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file=os.path.join(IMAGE_PATH, "right.png"))
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# ✅ Start the first card
next_card()

# ✅ Run main loop
window.mainloop()
