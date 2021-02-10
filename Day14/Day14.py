
import re
import time
import math


def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list.
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    reMatch = re.compile("mem\[(\d+)\] = (\d+)")

    with open(fileName, 'r') as file:
        fileList = file.readlines()

    maskList = []
    memoryList = []
    tempMemoryList = []
    for line in fileList:
        if "mask" in line:
            maskList.append(line.replace("mask = ", "").strip())
            memoryList.append(tempMemoryList)
            tempMemoryList = []
        else:
            m = reMatch.findall(line)
            tempMemoryList.append(m[0])

    memoryList.append(tempMemoryList)

    return maskList, memoryList[1:]

def partOne(maskList, memoryList):
    """
    Fill out memmory with calculated values.
    :param maskList: list of masks
    :param memoryList: list memmory commands
    :return:
    """

    memory = {}
    for index in range(len(maskList)):

        currentMaskOne = int(maskList[index].replace("X", "0"), 2)
        currentMaskZero = int(maskList[index].replace("X", "1"), 2)

        for command in memoryList[index]:

            memoryLocation = int(command[0])
            value = int(command[1])

            value = value | currentMaskOne
            value = value & currentMaskZero

            memory[memoryLocation] = value

    return memory

def partTwo(maskList, memoryList):
    """
    Fill out memmory with calculated values.
    :param maskList: list of masks
    :param memoryList: list memmory commands
    :return:
    """

    memory = {}
    for index in range(len(maskList)):

        currentMask = maskList[index]

        for command in memoryList[index]:
            memoryLocation = bin(int(command[0]))[2:]
            value = int(command[1])
            tempMask = ""
            for index, bit in enumerate(memoryLocation[::-1]):
                if currentMask[-index - 1] == "0":
                    tempMask += bit
                else:
                    tempMask += currentMask[-index - 1]

            tempMask = tempMask[::-1]
            tempMask = currentMask[:-len(tempMask)] + tempMask

            maskAddresses = []
            recursiveFind(tempMask, len(tempMask) - 1, 0, maskAddresses)

            for entry in maskAddresses:
                memory[entry] = value

    return memory

def recursiveFind(currentMask, potency, sum, maskAddresses):


    if not currentMask:
        maskAddresses.append(sum)
        return

    if currentMask[0] == "X":
        recursiveFind(currentMask[1:], potency - 1, sum + math.pow(2, potency), maskAddresses)
        recursiveFind(currentMask[1:], potency - 1, sum, maskAddresses)

    else:
        recursiveFind(currentMask[1:], potency - 1, sum + math.pow(2, potency) * int(currentMask[0]), maskAddresses)



if __name__ == "__main__":

    maskList, memoryList = readInput("input.txt")
    print(f"maskList: {maskList}, memoryList: {memoryList}")

    memoryValueList = partOne(maskList, memoryList)
    print(f"Part 1: {(sum(memoryValueList.values()))}")

    memoryValueList = partTwo(maskList, memoryList)
    print(f"Part 2: {(sum(memoryValueList.values()))}")
