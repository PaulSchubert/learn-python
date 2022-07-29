import random

highest = 10
answer = random.randint(1, highest)
print(answer) #TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())

while guess != answer and guess != 0:

    if guess == answer:
        print("Correct!")
        break
    elif guess < answer:
        print("Guess higher")
    else:
        print("Guess lower")
    guess = int(input())

