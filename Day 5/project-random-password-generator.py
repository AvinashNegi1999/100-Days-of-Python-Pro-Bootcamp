#project to make random password generator

import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '?', '/', '\\', '{', '}', '[', ']']

print("Welcome to the PyPassword Generator!\n")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_numbers=int(input("how many numbers would you like?\n"))
nr_symbols=int(input("how many symbols would you like?\n"))

#easy level
# encrypt_code=""
# for number in range(0,nr_letters):
#     index=random.randint(0,25)
#     encrypt_code+=alphabet[index]
# print(encrypt_code)    

# for number in range(0,nr_numbers):
#     index=random.randint(0,9)
#     encrypt_code+=str(numbers[index])

# for number in range(0,nr_symbols):
#     index=random.randint(0,19)
#     encrypt_code+=symbols[index]

# print(encrypt_code)


#hard level
encrypt_code_list=[]
for number in range(0,nr_letters):
    index=random.randint(0,25)
    encrypt_code_list+=alphabet[index] 

for number in range(0,nr_numbers):
    index=random.randint(0,9)
    encrypt_code_list+=str(numbers[index])

for number in range(0,nr_symbols):
    index=random.randint(0,19)
    encrypt_code_list+=symbols[index]

print(encrypt_code_list)

random.shuffle(encrypt_code_list)

password=""

for char in encrypt_code_list:
    password+=char

print(f"your final encrypted password is {password}")