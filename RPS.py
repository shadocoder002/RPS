import random
print("Welcome to Rock Paper Scissors!")
def gameselect():
    selection = input("Rock Paper or Scissors? Respond with r, p, or s ").lower()
    if selection == "r":
        selection = 0
        rselect = "rock"
    elif selection == "p":
        selection = 1
        rselect = "paper"
    elif selection == "s":
        selection = 2
        rselect = "scissors"
    else: print("Invalid selection!"); gameselect()
    print(f"You chose {rselect}")
    computer = random.randint(0, 2)

gameselect()