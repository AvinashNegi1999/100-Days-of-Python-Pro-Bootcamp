# ✅ Password Manager (Tkinter + JSON + Pyperclip)
# ! Features: Save / Search / Generate strong passwords
# ✅ Auto-copy password to clipboard
# TODO: Add more features like update & delete later

from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox, END
import pyperclip
import json


# * ---------------------------- SEARCHING THROUGH JSON FILE ------------------------------- #
def auto_search():
    path = r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 030\save_password.json"

    # ✅ Get the entered website
    website = entry_website.get()

    try:
        # ✅ Open JSON file and load as dictionary
        with open(path, "r") as file:
            data = json.load(file)

        # ✅ Search for the website
        if website in data:
            email_value = data[website]["email"]
            password_value = data[website]["password"]

            # ✅ Update entry fields
            entry_email.delete(0, END)
            entry_email.insert(0, email_value)

            entry_password.delete(0, END)
            entry_password.insert(0, password_value)

        else:
            messagebox.showinfo("Not Found", f"No details found for {website}")

    except FileNotFoundError:
        messagebox.showerror("Error", "No data file found yet ❌")

    except json.JSONDecodeError:
        messagebox.showerror("Error", "JSON file is empty or corrupted ❌")


# * ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    # ✅ Numbers
    numbers_list = list("0123456789")

    # ✅ Uppercase letters
    uppercase_list = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    # ✅ Lowercase letters
    lowercase_list = list("abcdefghijklmnopqrstuvwxyz")

    # ✅ Special characters (expanded)
    special_list = list("!@#$%^&*()-_=+[]{}|\\:;\"'<>,.?/`~§±µ¢£¥€¤°©®™•¶÷×")

    password_upper_letter = [choice(uppercase_list) for _ in range(randint(4, 5))]
    password_lower_letter = [choice(lowercase_list) for _ in range(randint(4, 5))]
    password_number = [choice(numbers_list) for _ in range(randint(2, 4))]
    password_symbol = [choice(special_list) for _ in range(randint(4, 5))]

    password_list = (
        password_upper_letter
        + password_lower_letter
        + password_number
        + password_symbol
    )

    # ✅ Shuffle in-place
    shuffle(password_list)

    # ✅ Convert list back to string
    password = "".join(password_list)

    entry_password.delete(0, END)  # ✅ Clear previous text
    entry_password.insert(0, password)
    pyperclip.copy(password)


# * ---------------------------- SAVE PASSWORD ------------------------------- #
def get_entry_text():
    """Retrieves text from the Entry widgets and saves to a JSON file."""
    entered_website = entry_website.get()
    entered_mail = entry_email.get()
    entered_password = entry_password.get()

    # ✅ Check for empty fields
    if not entered_website or not entered_mail or not entered_password:
        messagebox.showwarning(
            title="Empty Fields", message="Please fill in all fields before saving."
        )
        return

    # ✅ New data to add
    new_data = {entered_website: {"email": entered_mail, "password": entered_password}}

    try:
        # ✅ Try reading existing data
        with open(
            r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 030\save_password.json",
            "r",
        ) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        # ✅ If file doesn’t exist, create new one
        data = {}
    except json.JSONDecodeError:
        # ✅ If file is empty/corrupted, reset data
        data = {}

    # ✅ Update data with new entry
    data.update(new_data)

    try:
        # ✅ Write back to file
        with open(
            r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 030\save_password.json",
            "w",
        ) as data_file:
            json.dump(data, data_file, indent=4)
    except Exception as e:
        messagebox.showerror("Error", f"Could not save password: {e}")
    finally:
        # ✅ Always clear fields
        entry_website.delete(0, END)
        entry_password.delete(0, END)
        messagebox.showinfo("Success", "Password saved successfully ✅")


# * ---------------------------- UI SETUP ------------------------------- #
Windows = Tk()
Windows.title("Password Manager")
Windows.config(padx=20, pady=20)
Windows.columnconfigure(1, weight=1)

# ✅ Canvas (Logo Display)
canvas = Canvas(Windows, width=200, height=200, highlightthickness=0)
canvas.grid(row=0, column=1, pady=20)

logo_png = PhotoImage(
    file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 030\logo.png"
)
canvas.create_image(100, 100, image=logo_png)

# ✅ Labels
Label(text="Website:").grid(column=0, row=1)
Label(text="Email/Username:").grid(column=0, row=2)
Label(text="Password:").grid(column=0, row=3)

# ✅ Buttons
Button(text="Generate", command=random_password).grid(column=2, row=3)
Button(text="ADD", command=get_entry_text).grid(
    column=1, row=4, columnspan=2, sticky="ew"
)
Button(text="Search", command=auto_search).grid(column=2, row=1)

# ✅ Entry Fields
entry_website = Entry(Windows)
entry_website.grid(row=1, column=1, sticky="ew")
entry_website.focus()  # ✅ Auto-focus here when program starts

entry_email = Entry(Windows)
entry_email.insert(0, "avinashnegi1999work@gmail.com")  # ✅ Default email
entry_email.grid(row=2, column=1, columnspan=2, sticky="ew")

entry_password = Entry(Windows)
entry_password.grid(row=3, column=1, sticky="ew")  # left aligned

Windows.mainloop()
