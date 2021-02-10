
import re
import time
from lark import Lark

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:
        fileContent = file.read()

    return fileContent

def partOne(fileContent):
    """
    Check how many string are correct in according to the rules.
    :param fileContent: String that contains our entire file input. It consist of two parts. 1. are the rules. 2. are strings to check with a rules.
    :return:
    """

    splitContent =  fileContent.split("\n\n")

    ruleSet = re.sub(r'(\d+)', r'l\1', splitContent[0])

    larkObject = Lark(ruleSet, start='l0')
    validStrings = []
    for line in splitContent[1].split("\n"):
        try:
            larkObject.parse(line)
            validStrings.append(line)
        except:
            continue

    return len(validStrings)

def partTwo(fileContent):
    """
    Check how many string are correct in according to the rules.
    :param fileContent: String that contains our entire file input. It consist of two parts. 1. are the rules. 2. are strings to check with a rules.
    Replace rules:
    8: 42 -> 8: 42 | 42 8
    11: 42 31 -> 11: 42 31 | 42 11 31
    :return:
    """

    splitContent =  fileContent.split("\n\n")

    splitContent[0] = splitContent[0].replace("8: 42", "8: 42 | 42 8")
    splitContent[0] = splitContent[0].replace("11: 42 31", "11: 42 31 | 42 11 31")

    ruleSet = re.sub(r'(\d+)', r'l\1', splitContent[0])

    larkObject = Lark(ruleSet, start='l0')
    validStrings = []
    for line in splitContent[1].split("\n"):
        try:
            larkObject.parse(line)
            validStrings.append(line)
        except:
            continue

    return len(validStrings)

if __name__ == "__main__":

    fileContent = readInput("input.txt")
    print(f"fileContent: {fileContent}")

    numberOfCorrectStrings = partOne(fileContent)
    print(f"Part one: {numberOfCorrectStrings}")

    numberOfCorrectStrings = partTwo(fileContent)
    print(f"Part two: {numberOfCorrectStrings}")