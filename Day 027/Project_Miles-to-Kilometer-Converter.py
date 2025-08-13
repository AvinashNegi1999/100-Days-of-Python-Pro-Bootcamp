from tkinter import *

window = Tk()
window.geometry("800x600")
window.title("Miles to Kilometer converter")

# * Create a frame with padding around it
frame = Frame(window, padx=200, pady=200)
frame.pack(fill="both", expand=True)

# * Entry widget for miles input
entry = Entry(frame)
entry.grid(row=0, column=1, padx=10, pady=10)

# * Label displaying 'Miles'
miles = Label(frame, text="Miles", font=("Arial", 15, "bold"))
miles.grid(row=0, column=2, padx=10, pady=10)

# * Label displaying 'KM'
kilometer = Label(frame, text="KM", font=("Arial", 15, "bold"))
kilometer.grid(row=1, column=2, padx=10, pady=10)

# * Label displaying 'is equal to'
equal = Label(frame, text="is equal to", font=("Arial", 15, "bold"))
equal.grid(row=1, column=0, padx=10, pady=10)

# * Label to show conversion result (starts at 0)
my_label = Label(frame, text="0", font=("Arial", 15, "bold"))
my_label.grid(row=1, column=1, padx=10, pady=10)


# TODO: Create function to convert miles to kilometers on button click
def button_clicked():
    user_input = entry.get()
    try:
        user_input = float(user_input)
        kilometers = user_input * 1.60934
        my_label.config(text=f"{kilometers:.2f}")
    except ValueError:
        # ! Invalid input entered by user
        my_label.config(text="Invalid input")


# * Button to calculate conversion
calculate = Button(frame, text="Calculate", command=button_clicked)
calculate.grid(row=2, column=1, padx=10, pady=10)

window.mainloop()
