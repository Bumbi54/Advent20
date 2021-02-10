
import re
import operator
import time

def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    directionCommandsList = []
    reMatch = re.compile("([F,N,S,E,W,L,R]+)(\d+)")

    with open(fileName, 'r') as file:
        fileList = file.readlines()

    for directionCommands in fileList:
        m = reMatch.findall(directionCommands)
        directionCommandsList.append(m[0])

    return directionCommandsList



def steerShipPartTwo(directionCommandsList):
    """
    Steer ship by command directions.
    :param directionCommandsList: list of direction commands
    :return:
    """
    #first value is north or south. Second value is east or west. Integers.
    currentPosition = (0, 0)
    # first value is north or south. Second value is east or west. Binary.
    currentDirection = (1, 1)
    waypoint = (1, 10)

    directionDict = {
                    "N" : (1, 0),
                    "S" : (-1, 0),
                    "E" : (0, 1),
                    "W" : (0, -1),
                    }
    angleDict = {
                    1 : (1, 1),
                    2 : (1, 1),
                    3 : (1, 1),
                    }


    for directionCommand in directionCommandsList:

        if directionCommand[0] == "F":
            totalMovement = tuple(map(operator.mul, waypoint, (int(directionCommand[1]), int(directionCommand[1]) )))
            currentPosition = tuple(map(operator.add, currentPosition, totalMovement))

        elif directionCommand[0] in ["N", "S", "E", "W"]:
            tempDirection = directionDict[directionCommand[0]]
            tempWaypoint = tuple(map(operator.mul, (int(directionCommand[1]), int(directionCommand[1])), tempDirection))
            waypoint = tuple(map(operator.add, waypoint, tempWaypoint))


        elif directionCommand[0]  in ["R", "L"]:
            if directionCommand in [("R", "90"), ("L", "270")]:
                waypoint = (-waypoint[1], waypoint[0])

            elif directionCommand in [("R", "270"), ("L", "90")]:

                waypoint = (waypoint[1], -waypoint[0])

            elif "180" == directionCommand[1] :
                waypoint = (-waypoint[0], -waypoint[1])


    return currentPosition, currentDirection


def steerShip(directionCommandsList):
    """
    Steer ship by command directions.
    :param directionCommandsList: list of direction commands
    :return:
    """
    #first value is north or south. Second value is east or west. Integers.
    currentPosition = (0, 0)
    # first value is north or south. Second value is east or west. Binary.
    currentDirection = (0, 1)
    directionDict = {
                    "N" : (1, 0),
                    "S" : (-1, 0),
                    "E" : (0, 1),
                    "W" : (0, -1),
                    }
    angleDict = {
                    (1, 0) : 90,
                    (-1, 0) : 270,
                    (0, 1) : 0,
                    (0, -1) : 180,
                    }

    for directionCommand in directionCommandsList:

        if directionCommand[0] == "F":
            tempPosition = tuple(map(operator.mul, currentDirection, (int(directionCommand[1]), int(directionCommand[1]) )))
            currentPosition = tuple(map(operator.add, currentPosition, tempPosition))

        elif directionCommand[0] in ["N", "S", "E", "W"]:
            tempDirection = directionDict[directionCommand[0]]
            tempPosition = tuple(map(operator.mul, tempDirection, (int(directionCommand[1]), int(directionCommand[1]) )))
            currentPosition = tuple(map(operator.add, currentPosition, tempPosition))

        elif directionCommand[0]  in ["R", "L"]:

            angleDirection = angleDict[currentDirection]

            if directionCommand[0]  == "R":
                angleDirection = angleDirection - int(directionCommand[1])
            elif directionCommand[0]  == "L":
                angleDirection = angleDirection + int(directionCommand[1])

            if angleDirection in [-90, 270] :
                currentDirection = (-1, 0)
            elif angleDirection in [180, -180, 540]:
                currentDirection = (0, -1)
            elif angleDirection in [90, -270, 450]:
                currentDirection = (1, 0)
            elif angleDirection in [0, 360]:
                currentDirection = (0, 1)

    return currentPosition, currentDirection

if __name__ == "__main__":

    directionCommandsList = readInput("input.txt")
    print(f"directionCommandsList: {directionCommandsList}")

    currentPosition, currentDirection = steerShip(directionCommandsList)
    print(f"Part 1: currentPosition: {currentPosition}, currentDirection: {currentDirection}, Sum: {abs(currentPosition[0]) + abs(currentPosition[1])}")

    currentPosition, currentDirection = steerShipPartTwo(directionCommandsList)
    print(f"Part 2: currentPosition: {currentPosition}, currentDirection: {currentDirection}, Sum: {abs(currentPosition[0]) + abs(currentPosition[1])}")


