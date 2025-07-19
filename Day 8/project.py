# 💪 This is a difficult challenge! 💪

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.
# To work out the love score between two people:

# 1. Take both people's names and check for the number of times the letters in the word TRUE occur.
# 2. Then check for the number of times the letters in the word LOVE occur.
# 3. Combine these two totals to make a 2-digit number and print it out.

# Example:
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times → TRUE total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times → LOVE total = 3
# Love Score = 53

# Write your function below:

def calculate_love_score(name1, name2):
    # Convert both names to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count letters from "TRUE"
    true_score = 0
    for letter in "true":
        true_score += combined_names.count(letter)
        
    # Count letters from "LOVE"
    love_score = 0
    for letter in "love":
        love_score += combined_names.count(letter)
        
    # Combine the scores into a 2-digit number
    score = int(str(true_score) + str(love_score))
    
    # Print the result
    print(f"{score}")

# Call your function with hard coded values
calculate_love_score("Kanye West", "Kim Kardashian")
