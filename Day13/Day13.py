
import math
import time


def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    with open(fileName, 'r') as file:
        fileList = file.readlines()

    return int(fileList[0]), fileList[1].split(",")



def findBus(departureTime, busList):
    """
    Find bus that departs closes to our departure time
    :param departureTime: out departure time
    :param busList: list buses ride times
    :return:
    """
    validPasswords = []
    bestDepartureTIme = departureTime
    bestBus = 0
    for bus in busList:
        print(f"bus: {bus}")
        if bus != "x":

            tempDepartureTime = math.ceil(departureTime / int(bus)) *  int(bus)
            print(f"    tempDepartureTime: {tempDepartureTime}")

            differenceInTime = tempDepartureTime - departureTime

            if differenceInTime < bestDepartureTIme:
                bestDepartureTIme = differenceInTime
                bestBus = bus

    return bestDepartureTIme, int(bestBus)

def findTime(busList):
    """
    Second part.
    :param busList: list buses ride times
    :return:
    """
    validPasswords = []
    bestDepartureTIme = departureTime

    currentTime = 0
    currentBusPosition = 1
    incrementValue = int(busList[0])
    curentBusIndex = 1
    valuLis = [0, 0]


    while True:

        if curentBusIndex > len(busList) - 1:
            break

        currentTime +=  incrementValue

        if busList[curentBusIndex] == "x":
            curentBusIndex += 1
            currentBusPosition += 1

        elif (currentTime + curentBusIndex) % int(busList[curentBusIndex]) == 0:
            valuLis.append(currentTime)

            tempTime = currentTime
            while True:
                tempTime += incrementValue
                if (tempTime + curentBusIndex) % int(busList[curentBusIndex]) == 0:
                    incrementValue = tempTime - valuLis[-1]
                    curentBusIndex += 1
                    break

    return currentTime

if __name__ == "__main__":

    departureTime, busList = readInput("input.txt")
    print(f"departureTime: {departureTime}, busList: {busList}")

    #bestDepartureTIme, bestBus = findBus(departureTime, busList)
    #print(f"Part 1: {(bestDepartureTIme * bestBus)}")

    foundTime = findTime(busList)
    print(f"Part 2: {(foundTime)}")
