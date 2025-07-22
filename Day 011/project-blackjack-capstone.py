import random
from art import logo  # Importing logo ASCII art from external file
print(logo)

def deal_card():
    """Returns a random card from the deck (infinite deck assumption)"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 11 = Ace; face cards = 10
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """
    Takes a list of cards and returns the score calculated from the cards.
    Returns 0 if the hand is a Blackjack (two cards that sum to 21).
    Converts Ace (11) to 1 if the score is over 21.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 will represent Blackjack in this game

    if 11 in cards and sum(cards) > 21:
        # Replace one Ace from 11 to 1 to avoid busting
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    """
    Compares the user's score (u_score) and computer's score (c_score)
    Returns a result string indicating win/lose/draw.
    """
    if u_score == c_score:
        return "Draw 🙃"
    elif c_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif u_score == 0:
        return "Win with a Blackjack 😎"
    elif u_score > 21:
        return "You went over. You lose 😭"
    elif c_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > c_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    """Runs one complete round of Blackjack"""
    print(logo)  # Display game logo

    # Initialize user and computer card lists
    user_cards = []
    computer_cards = []

    # Initialize scores and game over flag
    computer_score = -1
    user_score = -1
    is_game_over = False

    # Deal 2 cards to user and computer at the start
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # User's turn: keep asking until game ends or user passes
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End the game if someone has Blackjack or user goes over 21
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask user if they want another card
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn: draw until score reaches at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Show final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    # Print game result
    print(compare(user_score, computer_score))

# Game loop: keeps running as long as user types 'y'
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)  # Clear screen by printing newlines
    play_game()
