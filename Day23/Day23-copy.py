
import re
import copy
from operator import mul
import time



def playGame(inputList):
    """
    Resolve the game of cups
    :param inputList: Start position of cups.
    :return:
    """

    currentPosition = 0

    round = 1
    while round < 11:
        print("#######################################")
        print(f"Round: {round}")
        currentCup = inputList[currentPosition]
        print(f"currentCup: {currentCup}")

        selectedCups = [inputList.pop( (inputList.index(currentCup) + 1) % len(inputList) )]
        selectedCups.append(inputList.pop( (inputList.index(currentCup) + 1) % len(inputList)))
        selectedCups.append(inputList.pop( (inputList.index(currentCup) + 1) % len(inputList)))
        print(f"selectedCups: {selectedCups}")
        print(f"inputList: {inputList}")

        destinationCup = currentCup - 1

        while destinationCup in selectedCups:
            print(f"Temp destinationCup: {destinationCup}")
            destinationCup -= 1

        if destinationCup < 1 or destinationCup not in inputList:
            destinationCup = max(inputList)

        print(f"destinationCup: {destinationCup}")

        targetedIndex = inputList.index(destinationCup) + 1

        print(f"targetedIndex: {targetedIndex}")

        inputList = inputList[:targetedIndex] + selectedCups + inputList[targetedIndex:]

        print(f"Resulting inputList: {inputList}")

        #currentPosition = (currentPosition + 1) % 9
        currentPosition = (inputList.index(currentCup) + 1) % 9



        print(f"New currentPosition: {currentPosition}")

        round += 1

    return  inputList


if __name__ == "__main__":

    inputString = "389125467"
    inputList = list(map(int, list(inputString)))

    print(inputList)
    result = playGame(inputList)

    string = ""
    print(f"Part 1: {result}")

    while len(result) > 1:
        string += str(result.pop( (result.index(1) + 1) % len(result) ))


    print(f"Part 1: {string}")


