from tkinter import *
import random

# * ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    # ✅ Numbers
    numbers_list = list("0123456789")

    # ✅ Uppercase letters
    uppercase_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # ✅ Lowercase letters
    lowercase_list = list("abcdefghijklmnopqrstuvwxyz")

    # ✅ Special characters (expanded)
    special_list = list("!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~§±µ¢£¥€¤°©®™•¶÷×")

    # * Step 1: Collect random characters
    password_chars = []
    for _ in range(3):
        password_chars.append(random.choice(numbers_list))
    for _ in range(3):
        password_chars.append(random.choice(uppercase_list))
    for _ in range(3):
        password_chars.append(random.choice(lowercase_list))
    for _ in range(3):
        password_chars.append(random.choice(special_list))

    # * Step 2: Shuffle the list for randomness
    random.shuffle(password_chars)

    # * Step 3: Convert list into a string (beginner-friendly method)
    final_password = ""
    for char in password_chars:
        final_password += char

    # * Step 4: Put password in entry box
    entry_password.delete(0, END)       # ✅ Clear previous text
    entry_password.insert(0, final_password)  # ✅ Insert new password


# * ---------------------------- SAVE PASSWORD ------------------------------- #
def get_entry_text():
    """Retrieves text from the Entry widgets and saves to a file."""
    # ✅ Get user inputs
    entered_text = entry_website.get()
    entered_mail = entry_email.get()
    entered_password = entry_password.get()

    # ! Warning: "w" mode will overwrite previous saved data — use "a" to append if needed
    with open(
        r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 029\save_password.txt",
        mode="a",
    ) as final_file:
        final_file.write(f"{entered_text} | {entered_mail} | {entered_password}")


# * ---------------------------- UI SETUP ------------------------------- #
Windows = Tk()
Windows.title("Password Manager")
Windows.config(padx=20, pady=20)
Windows.columnconfigure(1, weight=1)

# ✅ Canvas (Logo Display)
canvas = Canvas(Windows, width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1, pady=20)

logo_png = PhotoImage(
    file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 029\logo.png"
)
canvas.create_image(100, 100, image=logo_png)

# ✅ Labels
Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

# ✅ Buttons
Button(text="Generate", command=password).grid(column=2, row=3)
Button(text="ADD", command=get_entry_text).grid(
    column=1, row=4, columnspan=2, sticky="ew"
)

# ✅ Entry Fields
entry_website = Entry(Windows)
entry_website.grid(row=1, column=1, columnspan=2, sticky="ew")

entry_email = Entry(Windows)
entry_email.grid(row=2, column=1, columnspan=2, sticky="ew")

entry_password = Entry(Windows)
entry_password.grid(row=3, column=1, sticky="w")  # left aligned

Windows.mainloop()
