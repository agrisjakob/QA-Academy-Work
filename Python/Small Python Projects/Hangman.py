import random
exampleWord = ["s", "e", "a", "g", "u", "l", "l"]
exampleWord2 = ["t","o", "m", "a", "t", "o"]
exampleWord3 = ["m", "i", "r", "r", "o", "r"]
exampleWords = [exampleWord] + [exampleWord2] + [exampleWord3]

# A function that chooses a word from a set that the player has to guess.
def randomWord():
    return random.choice(exampleWords)
word = randomWord()
answer = list(len(word) * '-')

lives =6


def guessing():
    endGame = False
    guess = str(input('write your letter'))
    losingLife = 0
    isTheLetterInTheWord = False
    #Checks if the guessed letter matches any position in the word, adds it to the correct position in the 'answer' list 
    # and if it a letter matches, prevents the player from losing a life via  isTheLetterinTheWord = True
    if answer != word:
        for index in range(int(len(word))):
                for letter in word:
                  if guess == word[index]:
                   answer[index] = guess
                   isTheLetterInTheWord = True
    #Takes away a life if the guess didn't match any of the letters in the word
    if isTheLetterInTheWord == False:
        global lives
        lives -=1
        print("You have " + str(lives) + " lives left")
    #Prints each letter in the list 'answer' on the same line   
    for letter in answer:
        print(letter, end = " ")
    print()
    if lives == 0:
        print("You lost")
    if answer == word:
        print("You win")
        endGame = True
    return endGame

restartGame = False

while restartGame == False:
    while answer != word:
           restartGame = guessing()
           if lives == 0:

               break
    lives = 6
    print("Do you want to restart the game?")
    response = str(input("Yes/No"))
    if response == "Yes" or response == "yes":
        restartGame = False
        word = randomWord()
        answer = list(len(word) * '-')
    else:
        print("Thanks for playing.")




