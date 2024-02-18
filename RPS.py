import random
import msvcrt as m
print("Welcome to Rock Paper Scissors!")
def gameselect():
    global selection
    global computer
    global cselect
    selection = input("Rock Paper or Scissors? Respond with r, p, or s: ").lower()
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
    if computer == 0: cselect = "rock"
    if computer == 1: cselect = "paper"
    if computer == 2: cselect = "scissors"


def decision():
    if selection == computer:
        print("Draw!", end=" ")
    elif selection == 0 and computer == 1:
        print("Computer Won.", end=" ")
    elif selection == 0 and computer == 2:
        print("Player Won.", end=" ")
    elif selection == 1 and computer == 0:
        print("Player Won.", end=" ")
    elif selection == 1 and computer == 2:
        print("Computer Won.", end=" ")
    elif selection == 2 and computer == 0:
        print("Computer Won.", end=" ")
    elif selection == 2 and computer == 1:
        print("Player Won.", end=" ")

    print(f"Computer chose {cselect}")

while True:
    gameselect()
    decision()
    print("Press any key to play another game.", end="\n"*3)
    #m.getch()
