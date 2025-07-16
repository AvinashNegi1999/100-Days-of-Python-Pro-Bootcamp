print("welcome to rollercoaster ride")
height=int(input("enter you height: "))

if height>120:
    print("you can go in rollercoaster")
    age=int(input("enter you age: "))
    if age<=18:
        print("please pay 7$.")
    else:
        print("please pay 12$")
else:
    print("sorry you have to grow taller before you can ride.")