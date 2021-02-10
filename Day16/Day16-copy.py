
import re
import copy
import time

def parseTickets(fileName):
    """
    Read input file and parse it into list of group. Parse each group into list of people
    :param fileName: name of input file
    :return: list of groups
    """

    fieldsDict = {}
    fieldsList = []
    othersTicketsList = []
    fieldPattern = re.compile(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)')
    with open(fileName, 'r') as file:
        fileString = file.read()

    unparsedInputist = fileString.split("\n\n")
    print(f"unparsedInputist : {unparsedInputist}")

    #parse fields
    for field in unparsedInputist[0].split("\n"):
        m = re.search(fieldPattern, field)
        firstInterval = (int(m[2]), int(m[3]))
        secondInterval = (int(m[4]), int(m[5]))

        fieldsDict[m[1]] = [ firstInterval, secondInterval ]
        fieldsList.append(firstInterval)
        fieldsList.append(secondInterval)

    print(fieldsList)
    print(fieldsDict)

    #parse our ticket
    ourTicketList = list(map(int, unparsedInputist[1].split("\n")[1].split((",")) ))
    print(ourTicketList)

    #parse others tickets
    for field in unparsedInputist[2].split("\n")[1:]:
        othersTicketsList.append(list(map(int, field.split(","))))

    print(othersTicketsList)

    return fieldsDict, fieldsList, ourTicketList, othersTicketsList

def countYesAnswers(groupsList):
    """
    Count how many different yes answers are in each group
    :param groupsList: List of dictionaries that represent passport
    :return: total number of yes unique (per group) answers in all groups
    """

    numberOfYesAnswers = 0

    for group in groupsList:

        groupYesAnswers = set()
        for person in group:
            for answer in person:
                groupYesAnswers.add(answer)
        numberOfYesAnswers += len(groupYesAnswers)

    return numberOfYesAnswers

def countYesAnswersPartTwo(groupsList):
    """
    Count how many  yes answers are in each group. Answer is counted as yes only if everybody in groups answered yes on it.
    :param groupsList: List of dictionaries that represent passport
    :return: total number of yes unique (per group) answers in all groups
    """

    numberOfYesAnswers = 0

    for group in groupsList:

        groupYesAnswers = {}
        for person in group:
            for answer in person:
                if answer in groupYesAnswers.keys():
                    groupYesAnswers[answer] += 1
                else:
                    groupYesAnswers[answer] = 1

        for key,value in groupYesAnswers.items():

            if value == len(group):
                numberOfYesAnswers += 1

    return numberOfYesAnswers

def partOne(fieldsList, othersTicketsList):
    """
    Find values in other people ticket that don't match any interval.
    :param fieldsList:
    :param othersTicketsList:
    :return:
    """

    invalidFields = []
    invalidTickets = []
    for otherPersonList in othersTicketsList:
        for field in otherPersonList:

            invalidFlag = True
            for interval in fieldsList:

                if interval[0] <= field <= interval[1]:
                    invalidFlag = False

            if invalidFlag:
                invalidFields.append(field)
                invalidTickets.append(otherPersonList)
                break

    print(f"invalidTickets: {invalidTickets}")
    for ticket in invalidTickets:
        othersTicketsList.remove(ticket)

    return invalidFields

def partTwo(fieldsDict, fieldsList, ourTicketList, othersTicketsList ):
    """
    Find field order.
    :param fieldsDict:
    :param fieldsList:
    :param ourTicketList:
    :param othersTicketsList:
    :return:
    """
    print("Part 2: ##########################################################")
    fieldMaping = {}

    for fieldName, fieldIntervals in fieldsDict.items():
        print(f"fieldName: {fieldName}, fieldInterval: {fieldIntervals}")

        potentialIndexs =  [i for i in range(len(ourTicketList))]
        potentialIndexs = set(potentialIndexs)
        print(f"    potentialIndexs: {potentialIndexs}")

        for ticket in othersTicketsList:
            print(f"    Current ticket: {ticket}")
            for index, field in enumerate(ticket):

                validInterval = False
                for specificInterval in fieldIntervals:

                    if specificInterval[0] <= field <= specificInterval[1]:
                        validInterval = True

                if not validInterval:
                    potentialIndexs.remove(index)

        print(f"    Resulting potentialIndexs: {potentialIndexs}")
        fieldMaping[fieldName] = potentialIndexs

    print(f"    Temp fieldMaping: {fieldMaping}")

    while True:

        singleton = []
        tempDict = {}
        for key, value in fieldMaping.items():

            if len(value) == 1:
                fieldMaping[key] = value
                singleton.append(value)
            else:
                tempDict[key] = value

        for singleValue in singleton:
            for key, value in tempDict.items():
                print(f"value: {value}")
                print(f"singleValue: {singleValue}")
                for temp in singleValue:
                    if temp in value:
                        value.remove(temp)

        print(f"fieldMaping: {fieldMaping}")
        print(f"tempDict: {tempDict}")
        print(f"singleton: {singleton}")

        if len(singleton) ==  len(fieldMaping.keys()):
            break

        time.sleep(2)




    return fieldMaping


if __name__ == "__main__":

    fieldsDict, fieldsList, ourTicketList, othersTicketsList = parseTickets("input.txt")
    print(f"fieldsDict: {fieldsDict}, fieldsList: {fieldsList}, ourTicketList: {ourTicketList}, othersTicketsList: {othersTicketsList}")

    invalidFields = partOne(fieldsList, othersTicketsList)
    print(f"Part 1: {sum(invalidFields)}")
    print(f"fieldsDict: {fieldsDict}, fieldsList: {fieldsList}, ourTicketList: {ourTicketList}, othersTicketsList: {othersTicketsList}")

    allTickets = othersTicketsList + [ourTicketList]
    fieldMaping = partTwo(fieldsDict, fieldsList, ourTicketList, allTickets )
    print(f"Part 2: {fieldMaping}")