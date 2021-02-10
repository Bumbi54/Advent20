
import math


def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            fileContent.append(line.strip())

        return fileContent

def findSeatNumbers(seatingList):
    """
    Parse list of seating using binary space partitioning algo
    :param seatingList: list of string that will be parsed
    :return:
    """
    seatNumberList = []
    for seatingString in seatingList:
        rowRange = [0, 127]

        for currentString in seatingString[:-3]:

            middle = (rowRange[0] + rowRange[1]) / 2

            if currentString == "F":
                rowRange[1] = math.floor(middle)
            elif currentString == "B":
                rowRange[0] = math.ceil(middle)
            #print(currentString)
            #print(rowRange)

        seatRange = [0, 7]
        for currentString in seatingString[-3:]:

            middle = (seatRange[0] + seatRange[1]) / 2

            if currentString == "L":
                seatRange[1] = math.floor(middle)
            elif currentString == "R":
                seatRange[0] = math.ceil(middle)
            #print(currentString)
            #print(seatRange)

        seatNumberList.append(rowRange[0] * 8 + seatRange[0])
        #print("##############################")

    return seatNumberList


if __name__ == "__main__":

    seatingList = readInput("input.txt")
    print(f"seatingList: {seatingList}")

    seatNumberList  = findSeatNumbers(seatingList)
    print(f"Part 1: {max(seatNumberList)}")

    for number in range(max(seatNumberList)):

        if number not in seatNumberList:
            print(f"Potential part 2: {number}")
