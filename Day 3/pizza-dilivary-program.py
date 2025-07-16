print("welcome to python pizza diliveries!")
size=input("what size do you want? S, M or L: ")
pepperoni=input("do you want pepperoni on your pizza? Y or N: ")
extra_cheese=input("do you want extra cheese? Y or N: ")

pizza_price=0
#if condition for size
if size=="S":
    print(" price of small pizza is 15$")
    pizza_price=15
elif size=="M":
    print("price of medium pizza is 20$")
    pizza_price=20
elif size=="L":
    print("price of large pizza is 25$")
    pizza_price=25
else: 
    print("you enter invalid input")
    exit()

#if condition for pepperoni
if pepperoni=="Y":
    if size=="S":
        pizza_price+=2
    else:
        pizza_price+=3

#if condition for extra cheese
if extra_cheese=="Y":
    pizza_price+=1

# final bill
print(f"final bill is {pizza_price}")
