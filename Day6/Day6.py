
import re
import json
import ast

def parseGroups(fileName):
    """
    Read input file and parse it into list of group. Parse each group into list of people
    :param fileName: name of input file
    :return: list of groups
    """

    groupsList = []
    with open(fileName, 'r') as file:
        fileString = file.read()

    unparsedGroupList = fileString.split("\n\n")

    for unparsedGroup in unparsedGroupList:

        peopleList = re.split(' |\n',unparsedGroup)

        groupsList.append(peopleList)

    return groupsList

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

if __name__ == "__main__":

    groupsList = parseGroups("input.txt")
    print(f"groupsList: {groupsList}")

    numberOfYesAnswers = countYesAnswers(groupsList)
    print(f"Part 1: {numberOfYesAnswers}")

    numberOfYesAnswers = countYesAnswersPartTwo(groupsList)
    print(f"Part 2: {numberOfYesAnswers}")

