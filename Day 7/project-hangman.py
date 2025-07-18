import random

print('''
 _                                                   
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
''')

print("Welcome to Hangman game, where you guess the word!")

word_list = ["cat", "umbrella", "sky", "laptop", "zebra", "notebook", "axe", "mountain", "river", "book"]
computer_choice = random.choice(word_list)

print("Psst! Word to guess (for testing):", computer_choice)

count = len(computer_choice)
lives = 6
blanks = ["_"] * count

stages = [  # From 6 lives to 0
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    '''
]

while "_" in blanks and lives > 0:
    print(stages[6 - lives])
    print("Word:", " ".join(blanks))
    user_letter = input("Enter a letter: ").lower()

    if user_letter in computer_choice:
        for i in range(count):
            if computer_choice[i] == user_letter:
                blanks[i] = user_letter
        print("✅ Correct!")
    else:
        lives -= 1
        print("❌ Wrong!")

if "_" not in blanks:
    print("🎉 Congratulations! You guessed the word:", computer_choice)
else:
    print(stages[6 - lives])
    print("💀 You lost. The correct word was:", computer_choice)
