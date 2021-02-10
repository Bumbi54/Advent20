
import time
from operator import add

publicKey1 = 15113849
publicKey2 = 4206373


def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    with open(fileName, 'r') as file:
        return file.read().splitlines()

def partOne():
    """
    Resolve tile positions. And find their color.
    :param tileList:
    :return:
    """

    keyList = []

    value = 1
    subjectNumber = 7
    index = 1
    while len(keyList) < 2:
        value = value * subjectNumber
        value = value % 20201227

        #print(f"Round {index}, value: {value}")

        #if value in [5764801, 17807724] and index not in keyList.keys():
        if value in [publicKey1, publicKey2] :
            keyList.append((value, index))

        index += 1

    print(keyList)
    return keyList


def calculate(subjectNumber, loops):
    """
    Resolve tile positions. And find their color.
    :param tileList:
    :return:
    """

    value = 1
    for indey in range(1, loops + 1):
        value = value * subjectNumber
        value = value % 20201227

    return value

if __name__ == "__main__":

    #tileList = readInput("input.txt")
    #print(f"tileList: {tileList}")

    tileDict = partOne()
    print(f"Part 1: {tileDict}")

    encryptionKey1 = calculate(tileDict[0][0], tileDict[1][1])
    print(f"EncryptionKey 1: {encryptionKey1}")

    encryptionKey2 = calculate(tileDict[1][0], tileDict[0][1])
    print(f"EncryptionKey 2: {encryptionKey1}")

    #finalTileDict = partTwo(tileDict)
    #print(f"Part 2: {len(finalTileDict)}")

    #validPasswords = checkPasswordsPartTwo(passwordPolicyList)
    #print(f"Part 2: {len(validPasswords)}")
