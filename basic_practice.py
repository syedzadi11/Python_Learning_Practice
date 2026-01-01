# ------------------ BASIC VARIABLES ------------------
name = "syeda"
age = 22
roll_no = 11
contact = 970968976
dpt = "cs"

info = (
    "Name:", name,
    "Age:", age,
    "Roll No:", roll_no,
    "Contact:", contact,
    "Department:", dpt
)
print(info)


# ------------------ EVEN / ODD CHECK ------------------
user = int(input("Enter a number: "))
if user % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# ------------------ LIST LOOP PRACTICE ------------------
names = ["haya", "sdjh", "hcdc", "kheujdh"]
for name in names:
    print(name)


# ------------------ BAND NAME GENERATOR ------------------
print("Welcome to the Band Name Generator!")
city = input("Which city did you grow up in? ")
pet = input("What is your pet's name? ")
print("Your band name could be: " + city + " " + pet)


# ------------------ STRING TO INT SUM ------------------
user1 = "5"
user2 = "5"
total_sum = int(user1) + int(user2)
print("Sum:", total_sum)


# ------------------ BMI CALCULATOR ------------------
weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)


# ------------------ TIP CALCULATOR ------------------
print("Welcome to the Tip Calculator!")
bill = float(input("What is the total bill? "))
tip = float(input("How much tip would you like to give (%)? "))
people = int(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount
amount_per_person = round(total_bill / people, 2)

print(f"Each person should pay: {amount_per_person}")


# ------------------ SUM OF NUMBERS ------------------
total = 0
for num in range(1, 101):
    total += num
print("Sum from 1 to 100:", total)


# ------------------ LOGIN CHECK ------------------
p = "123"
if p == "123":
    print("Logged in")
else:
    print("Incorrect password")
