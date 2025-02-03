import random

randNum = random.randint(0,50)
guesses = 0

while True:
    guess = input("Enter a number between 0 and 50: ")
    if guess.isdigit():
        guess = int(guess)
        if not( 0 < guess < 50):
            print("Out of bounds")
            continue
    else:
        print("Not a number")
        continue


    guesses += 1

    if guess == randNum:
        print("Youre right")
        break
    elif guess < randNum:
        print("Guess higher")
        continue
    else:
        print("Guess lower")
    
print(f"Guesses: " , guesses)