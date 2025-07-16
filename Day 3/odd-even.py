# odd and even number
num=int(input("enter the natural number: "))

if num%2==0:
    print("number is even.")
    age=int(input("enter you age: "))
    if age<=18:
        print("please pay 7$.")
    else:
        print("please pay 12$")
else:
    print("number is odd.")