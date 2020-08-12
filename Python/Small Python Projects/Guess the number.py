import random
listRange = 100
numberList = list(range(1, listRange))

#Generates a random number
def generateNumber():
    return random.choice(numberList)

randomNumber = generateNumber()


#Tells the player if their guess is higher than the random number
def tooHigh(guess, randomNumber):
    if guess - randomNumber >= 1:
        print("Too high.")
#Tells the player if their guess is lower than the random number
def tooLow(guess, randomNumber):
    if randomNumber - guess >= 1:
        print("Too low.")

guessList = []

#Asks for the players input and adds it to a list of guesses
def guessing():
    guess = int(input("Guess the number: "))
    if guess > randomNumber:
        tooHigh(guess, randomNumber)
    elif guess < randomNumber:
        tooLow(guess, randomNumber)
    guessList.append(int(guess))
    return guess

def resetGuessList():
    guessList = []

#Runs the game, restarts it and ends it.
def theGame():
    endGame = False
    livesLeft = 6
    while endGame == False:
        index = 0
        startGame = str(input("Start a new game? Y/N: "))
        if startGame == "Y" or startGame == "y":
            print("Guess the number between 1 and " + str(listRange) + ".")
            while livesLeft > 0:
                    guess = guessing()
                    if guess == randomNumber:
                        print("You win!")
                        endGame = True
                        break
                    if index > 0:
                        if abs(randomNumber - guessList[index-1]) > abs(randomNumber - guessList[index]):
                            print("You're getting closer.")
                        elif abs(randomNumber - guessList[index-1]) == abs(randomNumber - guessList[index]):
                            print("You're as close as last time.")
                        else:
                            print("You were closer last time.")
                    index +=1
                    livesLeft = 6 - index
                    print("You have " + str(livesLeft) + " lives left.")
                    if livesLeft == 0:
                        print("Game over, the number was " + str(randomNumber) + ".")
        else:
            print("Thanks for playing!")
            break
        endGame = False
        index = 0
        livesLeft = 6
        resetGuessList()

theGame()

#I am still working on this code, as there seems to be a problem with the game reseting
