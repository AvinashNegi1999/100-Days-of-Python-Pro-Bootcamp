# program to give ticket for rollercoaster ride using if-else-elif conditions
print("welcome to rollercoaster ride")
height=int(input("enter you height: "))
price=0
if height>120:
    print("you can go in rollercoaster")
    age=int(input("enter you age: "))
    if age<=12:
        print("please pay 5$.")
        price+=5
    elif age<=18:
        print("please pay 7$.")
        price+=7
    else:
        print("please pay 12$")
        price+=12
else:
    print("sorry you have to grow taller before you can ride.")

if price!=0:
    picture=input("do you want to take a photo(y/n)")
    if picture=="y":
        price+=3
        print(f"your total amount is {price}$")
    else:
        print(f"your total amount is {price}$")