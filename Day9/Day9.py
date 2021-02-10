
import itertools as it


def parseInput(fileName):
    """
    Read input file and parse it into a preamble list and into a code list
    :param fileName: name of input file
    :return: tuple of preamble list and code list
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            fileContent.append(int(line.strip()))

        return (fileContent[:25], fileContent[25:])

def findErrorOnCode(preamble, code):
    """
    Find an error in code. Code entry is not correct if it is not equal to any sum of two number from preamble.
    Each code entry is added to end of preamble while first entry in preamble is removed.
    :param preamble:
    :param code:
    :return:
    """

    for codeEntry in code:

        allSumsOfPreamble = [sum(sumCombination) for sumCombination in list(it.combinations(preamble, 2))]

        if codeEntry in allSumsOfPreamble:
            preamble.append(codeEntry)
            preamble.pop(0)
        else:
            return codeEntry

def findContiguousSumInCode(entireCode, targetedSum):
    """
    In entire code (preamble + code) find entries whos sum gives targetedSum value
    :param entireCode:
    :param targetedSum:
    :return:
    """

    #print(entireCode)
    for index, startOfSum in enumerate(entireCode):

        currentSum = startOfSum
        currentList = [startOfSum]
        #print(f"Current start element: {index}, {startOfSum}")
        for newEntryToSum in entireCode[index + 1:]:
            #print(f" Current element: {newEntryToSum}")
            #print(f" Current sum: {currentSum}")
            currentSum += newEntryToSum
            currentList.append(newEntryToSum)
            if currentSum == targetedSum:
                return currentList
            elif currentSum > targetedSum:
                break






if __name__ == "__main__":

    (preamble, code) = parseInput("input.txt")
    print(f"(preamble, code): {(preamble, code)}")

    errorCode = findErrorOnCode(preamble, code)
    print(f"Part 1: {errorCode}")

    (preamble, code) = parseInput("input.txt")
    print(f"(preamble, code): {(preamble, code)}")

    sumList = findContiguousSumInCode(list(preamble) + list(code), errorCode)
    print(f"Part 2: {max(sumList) + min(sumList)}, {sumList}")
