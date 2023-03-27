import random
from datetime import datetime

# The following function will initialize the given list with wise expressions.
def initializeWiseExpressionsList():
    expressionsList = \
        [
            ['always', 'be', 'honest'],
            ['always', 'be', 'yourself'],
            ['always', 'deliver', 'quality'],
            ['believe', 'in', 'yourself'],
            ['cash', 'is', 'king'],
            ['commit', 'or', 'quit'],
            ['health', 'is', 'wealth'],
            ['laughter', 'is', 'medicine'],
            ['live', 'love', 'laugh'],
            ['knowledge', 'is', 'power'],
            ['practice', 'makes', 'permanent'],
            ['teamwork', 'dream', 'work'],
            ['trust', 'the', 'process']
        ]

    return expressionsList

# The following function will play the guessing game - meaning,
# by using a loop of the total required guesses, we will present to the player
# the current state of the expression he should completely guess until the
# expression will be fully guessed correctly.
def playGuessingGame(raffledExpression, guessedExpression,
                     totalOfRequiredGuesses):

    print("Welcome to the guessing game!\nGuessing the entire expression in "
          "less than 30 seconds will give you a 100 points bonus! GoodLuck!!\n")

    # Challenge: saving the current game starting time
    startGameTime = datetime.now()

    playerScore = 0
    # Running a loop until number of required guesses will be 0.
    while totalOfRequiredGuesses > 0:
        print(guessedExpression)
        print("\nPlease Enter a character: ")
        guessedCharacter = input()
        isCorrectGuess = False

        # Going over all the words in the raffled expression.
        for i in range(len(raffledExpression)):
            tempString = ""
            # Checking if the player guessed character exists in current word
            if raffledExpression[i].count(guessedCharacter) > 0:
                # In case the guessed character exists in the word - search it
                for j in range(len(raffledExpression[i])):
                    if guessedCharacter == raffledExpression[i][j]:
                        # Updating necessary variables
                        tempString += guessedCharacter
                        isCorrectGuess = True
                        totalOfRequiredGuesses -= 1
                    else:
                        # In case current character is different from guessed
                        # character - copy the existing character from guessed
                        # expression
                        tempString += guessedExpression[i][j]

                guessedExpression[i] = tempString

        # Update player score
        if isCorrectGuess:
            playerScore += 5
        else:
            playerScore -= 1

    # saving the current game end time and computing game total duration time
    endGameTime = datetime.now()
    gameDurationInSeconds = (endGameTime - startGameTime).total_seconds()

    if gameDurationInSeconds < 30:
        playerScore += 100

    print(guessedExpression)
    return playerScore


# Main function
if __name__ == '__main__':

    # Defining the game wise expressions list using an assist function
    wiseExpressionsList = initializeWiseExpressionsList()

    # Raffling a random expression from the above wise expressions list
    raffledExpression = random.choice(wiseExpressionsList)

    guessedExpression = []
    totalOfRequiredGuesses = 0

    # Building the player guessed expression as a list of '_' + counting
    # the number of total required guesses
    for i in range(len(raffledExpression)):
        guessedExpression.append("")
        for j in range(len(raffledExpression[i])):
            guessedExpression[i] += '_'
            totalOfRequiredGuesses += 1

    playerScore = playGuessingGame(raffledExpression, guessedExpression,
                                   totalOfRequiredGuesses)

    print("\nThe game has finished. Your score is: ", playerScore)
