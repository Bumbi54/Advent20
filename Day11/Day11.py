
import re
import operator
import time

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:
        fileContent = file.readlines()

    return fileContent

def parseInputFile(fileContent):
    """
    Parse input file into set mapping.
    """

    seatsMaping = set()
    x = 0
    y = 0
    for line in fileContent:
        for location in line:
            if location == "L":
                seatsMaping.add((x, y))

            if location == "\n":
                y = 0
                x += 1
            else:
                y += 1

    return seatsMaping, x + 1, y

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

def simulateSeating(seatsMaping):
    """
    Simulate seating algorithm
    :param seatsMaping: set of coordinates with free seats
    :return:
    """

    adjacency = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    currentFreeSeats = seatsMaping.copy()
    currentOccupiedSeats = set()
    #stepFreeSeats = currentFreeSeats.copy()
    #stepOccupiedSeats = currentOccupiedSeats.copy()

    #printSeats(stepFreeSeats, stepOccupiedSeats)
    while True:
        stepFreeSeats = set()
        stepOccupiedSeats = set()
        for freeSeat in currentFreeSeats:

            noNeighborFlag = True
            for neighborOperation in adjacency:

                #neighbor = tuple(map(operator.add, neighborOperation, freeSeat))
                neighbor = (freeSeat[0] + neighborOperation[0], freeSeat[1] + neighborOperation[1])
                if neighbor in currentOccupiedSeats:
                    noNeighborFlag = False
                    break

            if noNeighborFlag:
                stepOccupiedSeats.add(freeSeat)
            else:
                stepFreeSeats.add(freeSeat)

        for occupiedSeat in currentOccupiedSeats:

            neighborCount = 0
            for neighborOperation in adjacency:

                #neighbor = tuple(map(operator.add, neighborOperation, occupiedSeat))
                neighbor = (occupiedSeat[0] + neighborOperation[0] , occupiedSeat[1] + neighborOperation[1]  )
                if neighbor in currentOccupiedSeats:
                    neighborCount += 1

                if neighborCount >= 4:
                    break

            if neighborCount >= 4:
                stepFreeSeats.add(occupiedSeat)
            else:
                stepOccupiedSeats.add(occupiedSeat)


        #print(stepFreeSeats)
        #print(stepOccupiedSeats)

        if currentFreeSeats == stepFreeSeats:
            break
        currentFreeSeats = stepFreeSeats
        currentOccupiedSeats = stepOccupiedSeats
        #printSeats(currentFreeSeats, currentOccupiedSeats)

    #printSeats(currentFreeSeats, currentOccupiedSeats)
    return currentFreeSeats, currentOccupiedSeats

def simulateSeatingPartTwo(seatsMaping, max_X, max_Y):
    """
    Simulate seating algorithm for part two
    :param seatsMaping: set of coordinates with free seats
    :return:
    """

    adjacency = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    currentFreeSeats = seatsMaping.copy()
    currentOccupiedSeats = set()
    #stepFreeSeats = currentFreeSeats.copy()
    #stepOccupiedSeats = currentOccupiedSeats.copy()

    #printSeats(stepFreeSeats, stepOccupiedSeats)
    while True:

        stepFreeSeats = set()
        stepOccupiedSeats = set()
        for freeSeat in currentFreeSeats:

            noNeighborFlag = True
            for neighborOperation in adjacency:

                neighbor = freeSeat
                while True:
                    #time.sleep(1)
                    neighbor = (neighborOperation[0] + neighbor[0], neighborOperation[1] + neighbor[1])

                    if neighbor in currentOccupiedSeats:
                        noNeighborFlag = False

                    if neighbor[0] < 0 or neighbor[0] == max_X :
                        break

                    if neighbor[1] < 0 or neighbor[1] == max_Y :
                        break

                    if neighbor in currentFreeSeats or neighbor in currentOccupiedSeats:
                        break

                if not noNeighborFlag:
                        break

            if noNeighborFlag:
                stepOccupiedSeats.add(freeSeat)
            else:
                stepFreeSeats.add(freeSeat)

        for occupiedSeat in currentOccupiedSeats:

            neighborCount = 0
            for neighborOperation in adjacency:

                neighbor = occupiedSeat

                while True:
                    #time.sleep(1)


                    neighbor = (neighbor[0] + neighborOperation[0], neighbor[1] + neighborOperation[1])

                    if neighbor in currentOccupiedSeats:
                        neighborCount += 1

                    if neighbor[0] < 0 or neighbor[0] == max_X :
                        break

                    if neighbor[1] < 0 or neighbor[1] == max_Y :
                        break

                    if neighbor in currentFreeSeats or neighbor in currentOccupiedSeats:
                        break

                if neighborCount >= 5:
                    break

            if neighborCount >= 5:
                stepFreeSeats.add(occupiedSeat)
            else:
                stepOccupiedSeats.add(occupiedSeat)


        #print(stepFreeSeats)
        #print(stepOccupiedSeats)

        if currentFreeSeats == stepFreeSeats:
            break
        currentFreeSeats = stepFreeSeats
        currentOccupiedSeats = stepOccupiedSeats
        #printSeats(currentFreeSeats, currentOccupiedSeats)

    #printSeats(currentFreeSeats, currentOccupiedSeats)
    return currentFreeSeats, currentOccupiedSeats


if __name__ == "__main__":

    fileContent = readInput("input.txt")
    seatsMaping, max_X, max_Y = parseInputFile(fileContent)
    print(f"max_X: {max_X}, max_Y: {max_Y}, seatsMaping: {seatsMaping}")

    finalSeatMaping = simulateSeating(seatsMaping)
    print(f"Part 1: {len(finalSeatMaping[1])}")

    finalSeatMaping = simulateSeatingPartTwo(seatsMaping, max_X, max_Y)
    print(f"Part 2: {len(finalSeatMaping[1])}")
