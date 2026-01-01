import random
choice = ["rock, paper, scissors"]
user_choice = input("choose rock, paper or scissors: ").lower()
computer_choice = random.choice(choice)
print("computer choose:", computer_choice)
if user_choice == computer_choice:
    print("it's a draw")
elif user_choice == "rock" and computer_choice == "scissors":
    print("you win")
elif user_choice == "scissors" and computer_choice == "rock":
    print("you win")
elif user_choice == "scissor" and computer_choice == "paper":
    print("you win")
else:
    print("you lose!")