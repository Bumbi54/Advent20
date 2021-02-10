
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
    while round < 101:
        currentCup = inputList[currentPosition]

        selectedCups = [inputList.pop( (inputList.index(currentCup) + 1) % len(inputList) )]
        selectedCups.append(inputList.pop( (inputList.index(currentCup) + 1) % len(inputList)))
        selectedCups.append(inputList.pop( (inputList.index(currentCup) + 1) % len(inputList)))

        destinationCup = currentCup - 1

        while destinationCup in selectedCups:
            destinationCup -= 1

        if destinationCup < 1 or destinationCup not in inputList:
            destinationCup = max(inputList)


        targetedIndex = inputList.index(destinationCup) + 1

        inputList = inputList[:targetedIndex] + selectedCups + inputList[targetedIndex:]
        currentPosition = (inputList.index(currentCup) + 1) % 9

        round += 1

    return inputList

class Cup:
    def __init__(self, data):
        self.data = data
        self.next = None

def playGamePartOne(inputList):
    """
    Resolve the game of cups. With use of LinkedList.
    :param inputList: Start position of cups.
    :return:
    """

    objectDict = {}
    numberOfCups = 9

    #create cups objects and add them into dict so we can find specific cup object by its value
    for cup in inputList:
        objectDict[cup] = Cup(cup)

    #for each cup object next add cup object in line
    for index, cup in enumerate(inputList):
        objectDict[cup].next = objectDict[inputList[(index + 1) % len(inputList) ]]

    currentCup = objectDict[inputList[0]]

    round = 1
    while round < 101:

        #find next three cups from the current one
        firstCup = currentCup.next
        secondCup = firstCup.next
        thirdCup = secondCup.next

        threeCupsValue = [firstCup.data, secondCup.data, thirdCup.data]

        #calculate destination cup
        destinationValue = currentCup.data - 1

        while destinationValue in threeCupsValue:
            destinationValue -= 1

        if destinationValue < 1:
            destinationValue = numberOfCups
            while destinationValue in threeCupsValue:
                destinationValue -= 1
            destinationCup = objectDict[destinationValue]
        else:
            destinationCup = objectDict[destinationValue]

        #modify cup connections
        currentCup.next = thirdCup.next
        thirdCup.next = destinationCup.next
        destinationCup.next = firstCup

        #select next cup
        currentCup = currentCup.next
        round += 1

    return objectDict

def playGamePartTwo(inputList):
    """
    Resolve the game of cups. With use of LinkedList.
    :param inputList: Start position of cups.
    :return:
    """

    objectDict = {}
    numberOfCups = 1000000
    fullList = inputList + [i for i in range(10, 1000001)]

    #create cups objects and add them into dict so we can find specific cup object by its value
    for cup in fullList:
        objectDict[cup] = Cup(cup)

    #for each cup object next add cup object in line
    for index, cup in enumerate(fullList):
        objectDict[cup].next = objectDict[fullList[(index + 1) % len(fullList) ]]

    currentCup = objectDict[inputList[0]]

    print("Start with rounds:")

    round = 1
    while round < 10000001:

        #find next three cups from the current one
        firstCup = currentCup.next
        secondCup = firstCup.next
        thirdCup = secondCup.next

        threeCupsValue = [firstCup.data, secondCup.data, thirdCup.data]

        #calculate destination cup
        destinationValue = currentCup.data - 1

        while destinationValue in threeCupsValue:
            destinationValue -= 1

        if destinationValue < 1:
            destinationValue = numberOfCups
            while destinationValue in threeCupsValue:
                destinationValue -= 1
            destinationCup = objectDict[destinationValue]
        else:
            destinationCup = objectDict[destinationValue]

        #modify cup connections
        currentCup.next = thirdCup.next
        thirdCup.next = destinationCup.next
        destinationCup.next = firstCup

        #select next cup
        currentCup = currentCup.next
        round += 1

    return objectDict

if __name__ == "__main__":

    inputString = "523764819"
    inputList = list(map(int, list(inputString)))

    """
    print(inputList)
    result = playGame(inputList)

    string = ""
    while len(result) > 1:
        string += str(result.pop( (result.index(1) + 1) % len(result) ))
    print(f"Part 1: {string}")
    """

    objectDict = playGamePartTwo(inputList)
    print(f"Part 2: {objectDict[1].next.data * objectDict[1].next.next.data}")







