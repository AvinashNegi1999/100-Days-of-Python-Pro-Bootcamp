from tkinter import *  # → Import everything from tkinter for GUI
from quiz_brain import QuizBrain  # → Import QuizBrain class to handle quiz logic

THEME_COLOR = "#375362"  # → Define theme color for the quiz interface


class QuizInterface:
    # → Class to create the graphical user interface for the quiz

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # → Reference to the QuizBrain object

        # → Set up main window
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # → Score label
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # → Canvas for displaying question text
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,  # → x-coordinate of text center
            125,  # → y-coordinate of text center
            width=280,  # → Wrap text within 280 pixels
            text="Some Question Text",  # → Initial placeholder text
            fill=THEME_COLOR,  # → Text color
            font=("Arial", 20, "italic"),  # → Font style
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # → True button with image
        true_image = PhotoImage(
            file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 034\quizzler-app-start\images\true.png"
        )
        self.true_button = Button(
            image=true_image, highlightthickness=0, command=self.true_pressed
        )
        self.true_button.grid(row=2, column=0)

        # → False button with image
        false_image = PhotoImage(
            file=r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 034\quizzler-app-start\images\false.png"
        )
        self.false_button = Button(
            image=false_image, highlightthickness=0, command=self.false_pressed
        )
        self.false_button.grid(row=2, column=1)

        self.get_next_question()  # → Display the first question

        self.window.mainloop()  # → Start the Tkinter event loop

    def get_next_question(self):
        # → Reset canvas background color
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            # → Update score label
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # → Get the next question from QuizBrain
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            # ! Quiz finished, disable buttons and show final message
            self.canvas.itemconfig(
                self.question_text, text="You've reached the end of the quiz."
            )
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        # → Called when True button is pressed
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        # → Called when False button is pressed
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        # → Change canvas background based on correctness
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # → Wait 1 second then show the next question
        self.window.after(1000, self.get_next_question)
