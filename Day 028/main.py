from tkinter import *
import math

# * ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"  # ? Short break color
RED = "#e7305b"  # ? Long break color
GREEN = "#9bdeac"  # ? Work session color
YELLOW = "#f7f5dd"  # ? Background color
FONT_NAME = "Courier"
WORK_MIN = 0.1  # ? Work session in minutes (0.1 = 6 seconds)
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

reps = 0
timer = None


# * ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """! Reset the timer and UI to initial state"""
    window.after_cancel(timer)  # Stop the running timer
    canvas.itemconfig(timer_text, text="00:00")  # Reset timer text
    title_label.config(text="Timer", fg=GREEN)  # Reset title
    check_label.config(text="")  # Remove check marks
    start_button.config(state="normal")  # Re-enable start button
    global reps
    reps = 0


# * ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """! Start the Pomodoro timer"""
    start_button.config(state="disabled")  # Disable start button while timer runs
    global reps
    reps += 1  # Track the number of sessions

    # * Convert minutes to seconds
    work_sec = int(WORK_MIN * 60)
    short_break_sec = int(SHORT_BREAK_MIN * 60)
    long_break_sec = int(LONG_BREAK_MIN * 60)

    # ? Decide which session to start
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)  # Long break - red
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)  # Short break - pink
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN)  # Work session - green
        count_down(work_sec)


# * ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """! Countdown mechanism that updates timer every second"""
    count = int(count)  # ! Convert float to int to avoid display issues
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Format seconds as 2 digits
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()  # Start next session automatically

        # * Update check marks for completed work sessions
        marks = ""
        for _ in range(reps // 2):
            marks += "✔"
        check_label.config(text=marks, fg=GREEN)  # Check marks in green


# * ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# ? Canvas for tomato image and timer text
canvas = Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(
    file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 028\tomato.png"
)  # Ensure correct path
canvas.create_image(100, 112, image=tomato_png)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

# * Title label (Work/Break)
title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

# ? Check marks label
check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

# * Start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

# * Reset button
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
