import random

def main():
    user_score = 0
    computer_score = 0
    options = ['rock', 'paper', 'scissors']
    print("Welcome to Siddharth's rock paper scissors game vs computer random number generator.")
    
    while True:
        userInput = input("Enter rock, paper or scissors: ").lower()
        if userInput not in options:
            print("Error you dumbfuck! Enter correct name of move.")
            continue

        randNum = random.randint(0, 2)
        computer_move = options[randNum]

        
        if userInput == computer_move:
            print("Computer chose:", computer_move)
            print("It's a draw!")
        
        elif (userInput == 'rock' and computer_move == 'scissors') or \
             (userInput == 'paper' and computer_move == 'rock') or \
             (userInput == 'scissors' and computer_move == 'paper'):
            print("Computer chose:", computer_move)
            print("You won! Big W")
            user_score += 1
        
        else:
            computer_score += 1
            print("Computer chose:", computer_move)
            print("You lost against a computer dumbass!")

        
        user_in = input("Press Y to continue or Q to quit (like a loser): ").upper()
        while user_in not in ['Y', 'Q']:
            user_in = input("You must type Y or Q. Try again: ").upper()

        if user_in == 'Q':
            break

    print("Your score:", user_score)
    print("Computer score:", computer_score)

main()
