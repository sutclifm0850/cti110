#Random Number Guessing Game
#CTI 110 0901
#April 23, 2018
#Sutcliffe

import random

def generateRandomNumber():
    randomNumber = random.randint( 1, 100 )
    return randomNumber

def askUserForNumber( message = 'Guess the number: '):
    userNumber = int( input( message ))
    return userNumber

def checkUserNumber( userNumber, randomNumber ):
    if userNumber > randomNumber:
        return "Too high"
    elif userNumber < randomNumber:
        return "Too low"
    else:
        return "Congratulations!"

def main():
    playAgain = "y"

    while playAgain == "y":
        userNumberOfGuesses = 0
        randomNumber = generateRandomNumber()
        #print( 'For testing purposes, random number: ', randomNumber )
        userNumber = askUserForNumber()
        userNumberOfGuesses +=1
        message = checkUserNumber( userNumber, randomNumber )

        while message != "Congratulations!":
            print( message )
            userNumber = askUserForNumber( "Try again: " )
            userNumberOfGuesses +=1
            message = checkUserNumber( userNumber, randomNumber )

        print()
        print( message, "It took you", userNumberOfGuesses,\
            "attempts to guess correctly\n")
        playAgain = input( "Would you like to play again? type y for yes: ")

    print("\nThanks for playing" )

main()
