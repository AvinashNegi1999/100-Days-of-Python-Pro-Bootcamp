# Tip Calculator

bill = float(input("What was the total bill? "))
tip_percent = float(input("How much tip would you like to give? 10, 12, or 15: "))
split = float(input("How many people to split the bill? "))

tip = bill * tip_percent / 100  # Calculate tip
bill = bill + tip  # Add tip to bill
split = bill / split  # Split the total bill
split = round(split, 2)  # Round to 2 decimal places

print(f"Each person should pay: {split}")
