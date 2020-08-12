import random

game = str(input("Would you like to play? Y/N: "))
if game == "Y" or game == "y":
    playGame = True
else:
    playGame = False

while playGame == True:

    hand = str(input('Rock, paper or scissors?: '))

    actionList = ['rock', 'paper', 'scissors']

    computerPick = random.choice(actionList)



    print("You chose " + str(hand) + " and computer chose: " + str(computerPick))
    if hand == computerPick:
        print("It's a draw")
    elif hand == 'rock' and computerPick == 'paper':
        print("You Lose")
    elif hand == 'rock' and computerPick == 'scissors':
        print("You Win")
    elif hand == 'paper' and computerPick == 'rock':
        print("You Win")
    elif hand == 'paper' and computerPick == 'scissors':
        print("You lose")
    elif hand == 'scissors' and computerPick == 'paper':
        print("You win")
    elif hand == 'scissors' and computerPick == 'rock':
        print("You Lose")
    anotherGame = str(input("Play again? Y/N: "))
    if anotherGame == "Y" or game == "y":
        playGame = True
    else:
        playGame = False
