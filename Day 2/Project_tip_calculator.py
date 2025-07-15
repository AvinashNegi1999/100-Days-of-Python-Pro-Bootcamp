bill=float(input("what was the total bill? "))
tip_percent=float(input("how much tip would you like to give? 10, 12, or 15: "))
split=float(input("How many people to split the bill? "))

tip=bill*tip_percent/100
bill=bill+tip
split=bill/split
split=round(split,2)
print(f"each person should pay: {split}")