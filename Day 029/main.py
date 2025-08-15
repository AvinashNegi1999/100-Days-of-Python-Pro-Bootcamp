from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

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

    password_upper_letter=[choice(uppercase_list) for _ in range(randint(4,5))]
    password_lower_letter=[choice(lowercase_list) for _ in range(randint(4,5))]
    password_number=[choice(numbers_list) for _ in range(randint(2,4))]
    password_symbol=[choice(special_list) for _ in range(randint(4,5))]
   
    password_list = password_upper_letter + password_lower_letter + password_number + password_symbol

    # ✅ Shuffle in-place
    shuffle(password_list)

    # ✅ Convert list back to string
    password = "".join(password_list)

    
    entry_password.delete(0, END)  # ✅ Clear previous text
    entry_password.insert(0, password) 
    pyperclip.copy(password)



# * ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox

def get_entry_text():
    """Retrieves text from the Entry widgets and saves to a file."""
    # ✅ Get user inputs
    entered_text = entry_website.get()
    entered_mail = entry_email.get()
    entered_password = entry_password.get()

    # ! Step 1: Check for empty fields and stop immediately
    if entered_text == "" or entered_mail == "" or entered_password == "":
        messagebox.showwarning(
            title="Empty Fields",
            message="Please fill in all fields before saving."
        )
        return  # ✅ Stop function if any field is empty

    # * Step 2: Ask user to confirm details before saving
    is_ok = messagebox.askokcancel(
        title=entered_text,
        message=f"Website: {entered_text}\n"
                f"Email: {entered_mail}\n"
                f"Password: {entered_password}\n\n"
                "Is it ok to save?"
    )

    # ✅ Step 3: Save if confirmed
    if is_ok:
        try:
            with open(
                r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 029\save_password.txt",
                mode="a",
            ) as final_file:
                final_file.write(f"{entered_text} | {entered_mail} | {entered_password}\n")

            # ✅ Clear fields after saving
            entry_website.delete(0, END)
            entry_password.delete(0, END)

        except Exception as e:
            messagebox.showerror("Error", f"Could not save password: {e}")


    
    
    
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
Button(text="Generate", command=random_password).grid(column=2, row=3)
Button(text="ADD", command=get_entry_text).grid(
    column=1, row=4, columnspan=2, sticky="ew"
)

# ✅ Entry Fields
entry_website = Entry(Windows)
entry_website.grid(row=1, column=1, columnspan=2, sticky="ew")
entry_website.focus()  # ✅ Auto-focus here when program starts

entry_email = Entry(Windows)
entry_email.insert(0, "avinashnegi1999work@gmail.com")  # ✅ Default email
entry_email.grid(row=2, column=1, columnspan=2, sticky="ew")

entry_password = Entry(Windows)
entry_password.grid(row=3, column=1, sticky="w")  # left aligned

Windows.mainloop()
