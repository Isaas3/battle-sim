from os import system
import battle

while True:
    print("Welcome to my Text-Based Battle Simulator")

    print("1. State New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input(">>")

    if choice == "1":
        battle.start()
    elif choice == "2":
        print("Loading Game")
    elif choice == "3":
        print("You suck")
        exit(0)
    system("cls")
