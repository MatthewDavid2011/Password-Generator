import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the password generator!!!")
userletters = int(input("How many letters would you like in your password?"))
usersymbols = int(input("How many symbols would you like in your password?"))
usernumbers = int(input("How many numbers would you like in your password?"))
''''password= print(letters,symbols,numbers)
list = [letters,symbols, numbers]
random.shuffle(list)
print(list)'''
lettersstring = str(letters)
password= " "
for letter in range(1,userletters+1):
    random_letter= random.choice(letters)
    password+= random_letter
for symbol in range(1,usersymbols+1):
    random_symbol= random.choice(symbols)
    password+= random_symbol
for number in range(1,usernumbers+1):
    random_number= random.choice(numbers)
    password+= random_number
print(password)
password_list= list(password)
random.shuffle(password_list)
password_string = ''.join(password_list)
print(password_list)
print(password_string)
