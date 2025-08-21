from question_model import Question  #  Import the Question class
from data import question_data  #  Import the list of questions from data.py
from quiz_brain import QuizBrain  #  Import QuizBrain class to handle quiz logic
from ui import QuizInterface  #  Import the UI class for the quiz interface

question_bank = []  # → Initialize an empty list to store Question objects

for question in question_data:
    question_text = question["question"]  # → Extract the question text
    question_answer = question["correct_answer"]  # → Extract the correct answer
    new_question = Question(
        question_text, question_answer
    )  # → Create a Question object
    question_bank.append(
        new_question
    )  # → Add the Question object to the question_bank list

quiz = QuizBrain(question_bank)  # → Initialize QuizBrain with all questions
quiz_ui = QuizInterface(quiz)  # → Launch the quiz interface and pass the quiz logic
