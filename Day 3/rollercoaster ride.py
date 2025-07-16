# Program to give ticket for rollercoaster ride using if-else-elif conditions

print("Welcome to the rollercoaster ride!")
height = int(input("Enter your height in cm: "))
price = 0

if height > 120:
    print("You can go on the rollercoaster.")
    age = int(input("Enter your age: "))
    
    if age <= 12:
        print("Please pay $5.")
        price += 5
    elif age <= 18:
        print("Please pay $7.")
        price += 7
    else:
        print("Please pay $12.")
        price += 12

    picture = input("Do you want to take a photo (y/n)? ").lower()
    if picture == "y":
        price += 3

    print(f"Your final bill is ${price}.")
else:
    print("Sorry, you have to grow taller before you can ride.")