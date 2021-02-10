
import re
import copy
from operator import mul
import time


def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    playerOne = []
    playerTwo = []


    with open(fileName, 'r') as file:
        fileList = file.read()

    fileList = fileList.split("\n\nPlayer 2:\n")

    playerOne = fileList[0].split("\n")
    playerOne = list(map(int, playerOne[1:]))

    playerTwo = fileList[1].split("\n")
    playerTwo = list(map(int, playerTwo))

    return playerOne, playerTwo

def playGame(playerOne, playerTwo):
    """
    Resolve the game
    :param playerOne: initial cards in first player hand
    :param playerTwo:  initial cards in second player hand
    :return:
    """

    playerOneHand = copy.deepcopy(playerOne)
    playerTwoHand = copy.deepcopy(playerTwo)

    index = 1
    while(playerOneHand and playerTwoHand):
        playerOneCard = playerOneHand.pop(0)
        playerTwoCard = playerTwoHand.pop(0)

        if playerOneCard > playerTwoCard:
            playerOneHand.append(playerOneCard)
            playerOneHand.append(playerTwoCard)
        else:
            playerTwoHand.append(playerTwoCard)
            playerTwoHand.append(playerOneCard)

        index += 1

    print(f"playerOneHand: {playerOneHand}")
    print(f"playerTwoHand: {playerTwoHand}")

    finalList = playerOneHand + playerTwoHand
    mulList = list(range(len(finalList), 0, -1 ) )

    print(f"mulList: {mulList}")
    print(f"finalList: {finalList}")

    return  sum(map(mul, mulList, finalList))

def playGamePartTwo(playerOne, playerTwo, historyPlayerOne, historyPlayerTwo):
    """
    Resolve the game. Part two.
    :param playerOne: initial cards in first player hand
    :param playerTwo:  initial cards in second player hand
    :return:
    """

    #print("#########################################################################################################")
    #print(f"Entry into game: playerOne: {playerOne}, playerTwo: {playerTwo}, historyPlayerOne: {historyPlayerOne}, historyPlayerTwo:{historyPlayerTwo}")

    playerOneHand = copy.deepcopy(playerOne)
    playerTwoHand = copy.deepcopy(playerTwo)

    index = 1
    while(playerOneHand and playerTwoHand):

        #print(f"Round: {index}")
        #print(f"playerOneHand: {playerOneHand}")
        #print(f"playerTwoHand: {playerTwoHand}")

        if ''.join(str(e) for e in playerOneHand)  in historyPlayerOne or ''.join(str(e) for e in playerTwoHand) in historyPlayerTwo:
            #print("Repeat of history")
            #print(f"playerOneHand: {playerOneHand}, historyPlayerOne: {historyPlayerOne}")
            #print(f"playerTwoHand: {playerTwoHand},historyPlayerTwo:{historyPlayerTwo}")
            return ["win"], []
            break
        else:
            historyPlayerOne.add(''.join(str(e) for e in playerOneHand))
            historyPlayerTwo.add(''.join(str(e) for e in playerTwoHand))

        playerOneCard = playerOneHand.pop(0)
        playerTwoCard = playerTwoHand.pop(0)

        if len(playerOneHand) >= playerOneCard and len(playerTwoHand) >= playerTwoCard:
            playerOneResult, playerTwoResult = playGamePartTwo(playerOneHand[:playerOneCard], playerTwoHand[:playerTwoCard], set(), set() )

            if playerOneResult:
                playerOneHand.append(playerOneCard)
                playerOneHand.append(playerTwoCard)
            else:
                playerTwoHand.append(playerTwoCard)
                playerTwoHand.append(playerOneCard)

        else:
            if playerOneCard > playerTwoCard:
                #print("Player one wins")
                playerOneHand.append(playerOneCard)
                playerOneHand.append(playerTwoCard)
            else:
                #print("Player two wins")
                playerTwoHand.append(playerTwoCard)
                playerTwoHand.append(playerOneCard)

        index += 1

    #print(f"playerOneHand: {playerOneHand}")
    #print(f"playerTwoHand: {playerTwoHand}")

    #finalList = playerOneHand + playerTwoHand
    #mulList = list(range(len(finalList), 0, -1 ) )

    #print(f"mulList: {mulList}")
    #print(f"finalList: {finalList}")

    #print("---------------------------------------------------------------------------------------")
    #print("End of game")
    #time.sleep(1)

    return playerOneHand, playerTwoHand

    #return  sum(map(mul, mulList, finalList))

if __name__ == "__main__":

    playerOne, playerTwo = readInput("input.txt")
    print(f"playerOne: {playerOne}, playerTwo: {playerTwo}")

    result = playGame(playerOne, playerTwo)
    print(f"Part 1: {result}")

    result = playGamePartTwo(playerOne, playerTwo, set(), set() )

    finalList = result[0] + result[1]
    mulList = list(range(len(finalList), 0, -1 ) )
    print(f"Part 2: {sum(map(mul, mulList, finalList))}")
