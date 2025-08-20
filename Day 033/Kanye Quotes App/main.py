# ====================================================
# PROGRAM: Kanye Quote Generator
# AUTHOR : Avinash Negi
# PURPOSE: Fetches random Kanye West quotes from an API
#          and displays them on a GUI using Tkinter.
# ====================================================

from tkinter import *
import requests


# ---------------------------- FUNCTION ------------------------------- #
def get_quote():
    """
    Fetches a random Kanye West quote from the API and updates the canvas text.
    Adjusts font size based on quote length to keep it inside the canvas.
    """
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()  # ! Raises error if request fails

    data = response.json()  # ✅ Parse JSON response
    quote = data["quote"]  # ✅ Extract quote text

    # * Dynamically adjust font size based on quote length
    if len(quote) > 120:
        font_size = 16
    elif len(quote) > 80:
        font_size = 18
    elif len(quote) > 50:
        font_size = 22
    else:
        font_size = 26

    # * Update the existing canvas text with new quote and font size
    canvas.itemconfig(quote_text, text=quote, font=("Arial", font_size, "bold"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Kanye Says...")  # ✅ Window title
window.config(padx=50, pady=50)  # ✅ Padding around window

# * Canvas to hold background and quote text
canvas = Canvas(width=300, height=414)
background_img = PhotoImage(
    file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 033\Kanye Quotes App\background.png"
)
canvas.create_image(150, 207, image=background_img)

# * Initial quote text displayed on canvas
quote_text = canvas.create_text(
    150,
    207,
    text="Kanye Quote Goes HERE",
    width=250,  # ? Max width before wrapping text
    font=("Arial", 20, "bold"),
    fill="white",
)
canvas.grid(row=0, column=0)

# * Button to fetch a new Kanye quote
kanye_img = PhotoImage(
    file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 033\Kanye Quotes App\kanye.png"
)
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()  # ✅ Run the Tkinter event loop
