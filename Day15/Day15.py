
import time


def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        return  list(map(int, file.readline().split(",")))

class Number:
    def __init__(self, occurrence, lastTurnOccurrence, secondToLastTurnOccurrence):
        self.occurrence = occurrence
        self.lastTurnOccurrence = lastTurnOccurrence
        self.secondToLastTurnOccurrence = secondToLastTurnOccurrence

    def nextNumber(self):
        return self.lastTurnOccurrence - self.secondToLastTurnOccurrence

    def update(self, turnNumber):
        self.occurrence += 1
        self.secondToLastTurnOccurrence = self.lastTurnOccurrence
        self.lastTurnOccurrence = turnNumber

def playGame(inputNumbers, endOfGame):
    """
    Play the game until 2020th number is spoken.
    :param inputNumbers: list of numbers from which game starts.
    :param endOfGame: turn on which game ends
    :return: 2020th number spoken
    """

    turnNumber = len(inputNumbers) + 1
    numbersMemory = {}

    for index, number in enumerate(inputList):
        numbersMemory[number] = index + 1

    lastSpokenNumber = inputNumbers[-1]

    while turnNumber != endOfGame:
        lastSpokenNumberTime = numbersMemory.get(lastSpokenNumber, turnNumber - 1)
        nextNumber = turnNumber - 1 - lastSpokenNumberTime

        numbersMemory[lastSpokenNumber] = turnNumber - 1
        lastSpokenNumber = nextNumber
        turnNumber += 1

    return nextNumber

if __name__ == "__main__":

    inputList = readInput("input.txt")
    print(f"inputList: {inputList}")

    lastNumberSpoken = playGame(inputList, 2021)
    print(f"Part 1: {lastNumberSpoken}")

    lastNumberSpoken = playGame(inputList, 30000001)

    print(f"Part 2: {lastNumberSpoken}")