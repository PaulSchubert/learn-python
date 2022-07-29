availableExits = ["north", "south", "east", "west"]

chosenExit = ""

while chosenExit not in availableExits:
    chosenExit = input("Please chose a direction: ")
    if chosenExit.casefold() == "quit":
        print("Game over")
        break
