from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Miles to Kilometer converter")

# * Entry widget for miles input
entry = Entry(window)
entry.grid(row=0, column=1, padx=10, pady=10)

# * Label displaying 'Miles'
miles = Label(window, text="Miles", font=("Arial", 15, "bold"))
miles.grid(row=0, column=2, padx=10, pady=10)

# * Label displaying 'KM'
kilometer = Label(window, text="KM", font=("Arial", 15, "bold"))
kilometer.grid(row=1, column=2, padx=10, pady=10)

# * Label displaying 'is equal to'
equal = Label(window, text="is equal to", font=("Arial", 15, "bold"))
equal.grid(row=1, column=0, padx=10, pady=10)

# * Label to show conversion result (starts at 0)
my_label = Label(window, text="0", font=("Arial", 15, "bold"))
my_label.grid(row=1, column=1, padx=10, pady=10)

# * Function to convert miles to kilometers
def button_clicked():
    user_input = entry.get()
    try:
        user_input = float(user_input)
        kilometers = user_input * 1.60934
        my_label.config(text=f"{kilometers:.2f}")
    except ValueError:
        my_label.config(text="Invalid input")

# * Button to calculate conversion
calculate = Button(window, text="Calculate", command=button_clicked)
calculate.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
