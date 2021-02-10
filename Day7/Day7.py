
import re
from collections import deque

def readInput(fileName):
    """
    Read input file, parse lines into dictionary
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    bagMapping = {}
    reMatchBagMapping = re.compile("(.+) bags contain (.+).")
    reMatchContainBags = re.compile("(\d+) (.+) bag")

    with open(fileName, 'r') as file:
        fileList = file.readlines()

    for specificBagMapping in fileList:
        m = reMatchBagMapping.findall(specificBagMapping)[0]

        if m[0] not in bagMapping.keys():
            bagMapping[m[0]] = []

        containBags = m[1].split(", ")
        for bag in containBags:

            parsedBag = reMatchContainBags.findall(bag)
            if parsedBag:
                bagMapping[m[0]].append(parsedBag[0])

    return bagMapping


def checkValidBags333(bagMapping):
    """
    In a dictionary of passwords find bags that that contain shiny gold bag
    :param bagMapping: dictionary of bag mapping (what bags can each bag contain)
    :return:
    """
    notParsedQueues = deque()
    validBags = []

    for key, value in bagMapping.items():
        for bag in value:
            if bag[1] == "shiny gold":
                validBags.append(key)

    return validBags

def checkValidBags(bagMapping):
    """
    In a dictionary of passwords find bags that that contain shiny gold bag
    :param bagMapping: dictionary of bag mapping (what bags can each bag contain)
    :return:
    """
    notParsedQueues = deque()

    notParsedQueues.append("shiny gold")

    validBags = set()

    while notParsedQueues:
        currentBagCoolor = notParsedQueues.pop()
        for key, value in bagMapping.items():
            for bag in value:
                if bag[1] == currentBagCoolor:
                    validBags.add(key)
                    notParsedQueues.append(key)

    return validBags


def findNumberOfBagsWeCanCary(bagMapping):
    """
    In a dictionary of passwords find total number of bags we can cary in our shiny gold bag
    :param bagMapping: dictionary of bag mapping (what bags can each bag contain)
    :return:
    """
    notParsedQueues = deque()

    notParsedQueues.append(("shiny gold", 1))

    numberOfBags = 0

    while notParsedQueues:

        currentBagCoolor = notParsedQueues.pop()
        for subBags in bagMapping[currentBagCoolor[0]]:

            notParsedQueues.append( (subBags[1], int(subBags[0]) * currentBagCoolor[1]))
            numberOfBags += int(subBags[0]) * currentBagCoolor[1]


    return numberOfBags

if __name__ == "__main__":

    bagMapping = readInput("input.txt")
    print(f"bagMapping: {bagMapping}")

    validBags = checkValidBags(bagMapping)
    print(f"Part 1: {len(validBags)}")

    numberOfBags = findNumberOfBagsWeCanCary(bagMapping)
    print(f"Part 2: {numberOfBags}")
