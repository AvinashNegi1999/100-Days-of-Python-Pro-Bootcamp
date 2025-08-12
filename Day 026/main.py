# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
import pandas as pd

# Load CSV into a DataFrame
file_path = r"C:\Users\avina\OneDrive\Documents\GitHub\100-Days-of-Python-Code-challenge\Day 026\nato_phonetic_alphabet.csv"
df = pd.read_csv(file_path)

nato_list = {row["letter"]: row["code"] for index, row in df.iterrows()}

print(nato_list)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.

name_list = []
word = input("enter the word : ").upper()
for i in word:
    if i in nato_list:
        x = nato_list[i]
        name_list.append(x)

print(f"your name {word} has these code: {name_list}")
