# Import the ASCII art logo from art.py
from art import logo

# Print the welcome logo
print(logo)

# Function to find the highest bidder from the bidding dictionary
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0

    # Iterate over each bidder in the dictionary
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        # If current bid is greater than highest_bid, update
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    # Announce the winner
    print(f"\nThe winner is {winner} with a bid amount of ${highest_bid}.\n")

# Dictionary to store all bids
bids = {}

# Flag to control the while loop
continue_bidding = True

# Bidding loop
while continue_bidding:
    # Ask user for their name and bid
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price  # Add bid to the dictionary

    # Ask if there are more bidders
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)  # Call function to find and print the winner
    elif should_continue == "yes":
        print("\n" * 30)  # Clear the screen by printing blank lines
