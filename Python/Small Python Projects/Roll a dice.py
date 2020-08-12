import random
diceList = [1,2,3,4,5,6]
def diceRoll():
        print(random.choice(diceList))

restartGame = False
while restartGame == False:
        on = str(input("Roll the dice? Y/N: "))
        if on == "y" or on == "Y":
            diceRoll()
        else:
            restartGame = True
            print("Thanks for playing!")

