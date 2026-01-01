print("welcome to Treasure Island.")
print("Your mission is to find treasure.")
choice1 = input("Left or Right? ").lower()
if choice1 == "left":
    choice2 = input("swim or wait?").lower()
    if choice2 == "wait":
        choice3 = input("whice door? red, blue or yallow?").lower()
        if choice3 == "yallow":
            print("You win")
        elif choice3 == "red":
            print("Burned by fire. Game over")
        elif choice3 == "blue":
            print("Eaten by beasts. Game over")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")
