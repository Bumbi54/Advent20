
from itertools import product
import copy

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:
        fileContent = file.readlines()

    return fileContent

def parseInputFile(fileContent, dimensions):
    """
    Parse input file into set mapping.
    """

    startCoordinateSystem = set()
    x = 0
    y = 0
    for line in fileContent:
        for location in line:
            if location == "#":

                coordinate = (x, y)
                for newDimension in range(2, dimensions):
                    coordinate = coordinate + (0,)
                startCoordinateSystem.add(coordinate)

            if location == "\n":
                y = 0
                x += 1
            else:
                y += 1

    return startCoordinateSystem

def printSeats(stepFreeSeats, stepOccupiedSeats):

    for x_os in range(10):
        for y_os in range(10):
            coordinate = (x_os, y_os)
            if coordinate in stepFreeSeats:
                print("L", end='')
            elif coordinate in stepOccupiedSeats:
                print("#", end='')
            else:
                print(".", end='')
        print()

def sixCycles(startCoordinateSystem):
    """
    Caluclate systems state after 6 iterations. 3D system.
    :param startCoordinateSystem: set of coordinates that are initially set.
    :return:
    """

    tempCoordinateSystem = copy.deepcopy(startCoordinateSystem)

    for _ in range(6):
        newCoordinateSystem = set()
        # find all coordinate that can be changed.
        allCordinatesForCheck = set()
        for coordinate in tempCoordinateSystem:
            allCordinatesForCheck.update( set(product([coordinate[0] - 1, coordinate[0], coordinate[0] + 1], [coordinate[1] - 1, coordinate[1], coordinate[1] + 1], [coordinate[2] - 1, coordinate[2], coordinate[2] + 1])))

        for currentCoordinate in allCordinatesForCheck:

            neighbors = set(product([currentCoordinate[0] - 1, currentCoordinate[0], currentCoordinate[0] + 1],
                        [currentCoordinate[1] - 1, currentCoordinate[1], currentCoordinate[1] + 1],
                        [currentCoordinate[2] - 1, currentCoordinate[2], currentCoordinate[2] + 1]))

            neighbors.remove(currentCoordinate)

            neighborCheck = [1 for neighbor in neighbors if neighbor in tempCoordinateSystem]

            if currentCoordinate in tempCoordinateSystem and len(neighborCheck) in [2, 3]:
                newCoordinateSystem.add(currentCoordinate)
            elif len(neighborCheck) == 3:
                newCoordinateSystem.add(currentCoordinate)

        tempCoordinateSystem = newCoordinateSystem

    return newCoordinateSystem

def sixCyclesPartTwo(startCoordinateSystem):
    """
    Caluclate systems state after 6 iterations. 4D system.
    :param startCoordinateSystem: set of coordinates that are initially set.
    :return:
    """

    tempCoordinateSystem = copy.deepcopy(startCoordinateSystem)

    for _ in range(6):
        newCoordinateSystem = set()
        # find all coordinate that can be changed.
        allCordinatesForCheck = set()
        for coordinate in tempCoordinateSystem:
            allCordinatesForCheck.update(set(product([coordinate[0] - 1, coordinate[0], coordinate[0] + 1],
                                                     [coordinate[1] - 1, coordinate[1], coordinate[1] + 1],
                                                     [coordinate[2] - 1, coordinate[2], coordinate[2] + 1],
                                                     [coordinate[3] - 1, coordinate[3], coordinate[3] + 1]
                                                     )))

        for currentCoordinate in allCordinatesForCheck:
            neighbors = set(product([currentCoordinate[0] - 1, currentCoordinate[0], currentCoordinate[0] + 1],
                        [currentCoordinate[1] - 1, currentCoordinate[1], currentCoordinate[1] + 1],
                        [currentCoordinate[2] - 1, currentCoordinate[2], currentCoordinate[2] + 1],
                        [currentCoordinate[3] - 1, currentCoordinate[3], currentCoordinate[3] + 1]
                                    ))

            neighbors.remove(currentCoordinate)

            neighborCheck = [1 for neighbor in neighbors if neighbor in tempCoordinateSystem]

            if currentCoordinate in tempCoordinateSystem and len(neighborCheck) in [2, 3]:
                newCoordinateSystem.add(currentCoordinate)
            elif len(neighborCheck) == 3:
                newCoordinateSystem.add(currentCoordinate)

        tempCoordinateSystem = newCoordinateSystem

    return newCoordinateSystem

if __name__ == "__main__":


    fileContent = readInput("input.txt")
    startCoordinateSystem = parseInputFile(fileContent, 3)
    print(f"startCoordinateSystem: {startCoordinateSystem}")

    resultingSystem = sixCycles(startCoordinateSystem)
    print(f"Part 1: {len(resultingSystem)}")

    startCoordinateSystem = parseInputFile(fileContent, 4)
    print(f"startCoordinateSystem: {startCoordinateSystem}")

    resultingSystem = sixCyclesPartTwo(startCoordinateSystem)
    print(f"Part 2: {len(resultingSystem)}")
