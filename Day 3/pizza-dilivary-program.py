print("welcome to python pizza diliveries!")
size=input("what size do you want? S, M or L: ")
pepperoni=input("do you want pepperoni on your pizza? Y or N: ")
extra_cheese=input("do you want extra cheese? Y or N: ")

pizza_price=0
if size=="S":
    print(" price of small pizza is 15$")
    pizza_price=15
    if pepperoni=="Y":
        pizza_price+=2
elif size=="M":
    print("price of medium pizza is 20$")
    pizza_price=20
    if pepperoni=="Y":
        pizza_price+=3
elif size=="L":
    print("price of large pizza is 25$")
    pizza_price=25
    if pepperoni=="Y":
        pizza_price+=3
else: 
    print("you enter invalid input")

if extra_cheese=="Y":
    pizza_price+=1
else:
     print("you enter invalid input")


print(f"final bill is {pizza_price}")
