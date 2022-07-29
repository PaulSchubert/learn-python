low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
while low != high:
    guess = low + (high - low) // 2
    highLow = input("My guess is {}. Should I guess "
                    "higher or lowe? Enter h or l, or c if my guess "
                    "was correct. "
                    .format(guess)).casefold()

    if highLow == "h":
        #guess higher
        low = guess + 1

    elif highLow == "l":
        #guess lower
        high = guess + 1

    elif highLow == "c":
        print("I got it in {} guesses!".format(guesses))
        break

    else:
        print("Please enter a valid choice")

    guesses += 1

else:
    print("you thought of the number {}.".format(low))
    print("I got it in {}".format(guesses))