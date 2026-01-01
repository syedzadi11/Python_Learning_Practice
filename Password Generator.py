# import random

# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# numbers = ['0','1','2','3','4','5','6','7','8','9',]
# symbols = ['@','#','$','%','^','&','*']

# nr_letters = int(input("How many letters?"))
# nr_numbers = int(input("How many numbers"))
# nr_symbols = int(input("How many symbols"))

# password = ""

# for _ in range(nr_letters):
#     password += random.choice(letters)
# for _ in range(nr_numbers):
#     password += random.choice(numbers)
# for _ in range(nr_symbols):
#     password +=  random.choice(symbols)

# password_list = list(password)
# random.shuffle(password_list)

# final_password =""
# for char in password_list:
#     final_password += char

# print("Your password is :", final_password)




import random

letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
symbols = ['@', '#', '$', '%', '^', '&', '*']

nr_letters = int(input("How many letters? "))
nr_numbers = int(input("How many numbers? "))
nr_symbols = int(input("How many symbols? "))

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

final_password = "".join(password_list)

print("Your password is:", final_password)