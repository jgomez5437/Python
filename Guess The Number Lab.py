#Jesus Gomez Martinez
#22561 Prog & Prob Solv 2
#Guess The Number

"""This is a program that will allow the user to play a game where they guess a 
number between 1-1000."""
#Imports
import random
#This function is the main function that will call other functions.
def main():
    chosenNumber = random.randint(1,1000)
    playAgain = "yes"
    results = playGuessGame(chosenNumber)
    displayResults(results)
    askToPlayAgain(playAgain)
#This is the module that allows the user to play the game and tells them once they
#guessed the correct one.
def playGuessGame(chosenNumber):
    guessCounter = 0
    userNumber = 0
    try:
        userNumber = int(input("Guess my number between 1 and 1000 with the \
fewest guesses: "))
        guessCounter += 1
    except:
        print("Please enter a whole number.")     
    while userNumber != chosenNumber:
        if userNumber == chosenNumber:
            guessCounter += 1
            print("Congratulations. You guessed the number!")
            break
        elif userNumber < chosenNumber and userNumber != 0:
           try: 
            userNumber = int(input("Too low, try again: "))
            guessCounter += 1
           except:
            print("Please enter a whole number.") 
        elif userNumber > chosenNumber:
           try: 
            userNumber = int(input("Too high, try again: "))
            guessCounter += 1
           except:
            print("Please enter a whole number.")
        elif userNumber == 0:
           try: 
            userNumber = int(input("What's your guess?: "))
            guessCounter += 1
           except:
            print("Please enter a whole number.") 
    return guessCounter
#This module will display the number of guesses to the user.
def displayResults(results):
    if results < 10:
        print(f"Your number of guesses was {results}. \nEither you know the secret \
or you got lucky!")
    elif results > 10:
        print(f"Your number of guesses was {results}. \nYou should be able to do \
better!")
#This module will ask the player if they want to play again.
def askToPlayAgain(playAgain):
    response = str(input("Do you wish to play again? Type yes to continue: ")).lower()
    if response == playAgain:
        main()
    else:
        print("Thanks for playing!")
#This will call the main function.
main()