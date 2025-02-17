import random

randNum = random.randint(0,50)
guesses = 0

while True:
    guesses += 1
    userGuess = input("Enter a number between 0 and 50: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
        if not(0 <= userGuess <= 50):
            print("Out of bounds.")
            continue
    else:
        print("Not a digit.")
        continue

    if userGuess == randNum:
        print("You're right!")
        break
    elif userGuess <= randNum:
        print("Guess higher.")
    else:
        print("Guess lower.")

print("Total guesses:", guesses)
