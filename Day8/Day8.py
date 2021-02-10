
import re
import json
import ast
import time
import copy


class Machine:
    def __init__(self):
        self.accumulator = 0
        self.instructionHistory = set()
        self.instructionPosition = 0

    def proccesCommand(self, operation, argument):
        """
        Recieve command as two parameter "operation, argument" and call specific function dpenedin on "operation value".
        :param operation:
        :param argument:
        :return:
        """
        #print(f" Machine. operation: {operation}, argument: {argument}")
        #print(f" Machine. self.accumulator: {self.accumulator}")
        #print(f" Machine. self.instructionHistory: {self.instructionHistory}")
        #print(f" Machine. self.instructionPosition: {self.instructionPosition}")

        if operation == "nop":
            self.__noOperation()
        elif operation == "acc":
            self.__accumulatorChange(argument)
        elif operation == "jmp":
            self.__jump(argument)

        #print(f"  After Machine. self.accumulator: {self.accumulator}")
        #print(f"  After Machine. self.instructionHistory: {self.instructionHistory}")
        #print(f"  After Machine. self.instructionPosition: {self.instructionPosition}")


    def __noOperation(self):
        #Command 'nop +0'. Do nothing and just increase "instructionPosition" by one.
        self.instructionPosition += 1

    def __accumulatorChange(self, changeValue):
        """
        Change value in "self.accumulator" by value in parameter changeValue
        :param changeValue: value that will be added to "self.accumulator"
        :return:
        """
        self.accumulator += int(changeValue)
        self.instructionPosition += 1

    def __jump(self, offset):
        """
        Change "self.instructionPosition" by "offset" value
        :param offset : value that will be added to "self.instructionPosition"
        :return:
        """
        self.instructionPosition += int(offset)


def parseCommands(fileName):
    """
    Read input file and parse it into list of commands. Each entry is a tuple where first value is command operation and second value is command argument .
    :param fileName: name of input file
    :return: list of groups
    """

    commandList = []
    reMatchEntireCommand = re.compile("(.+) ([+-]+\d+)")

    with open(fileName, 'r') as file:
        fileList = file.readlines()

    for unparsedCommand in fileList:

        command = reMatchEntireCommand.findall(unparsedCommand)
        commandList.append(command[0])

    return commandList

def findInfiniteLoop(commandList):
    """
    Find command before the infinite loop starts.
    :param commandList: List of dictionaries that represent passport
    :return: command before the infinite loop,  its index and accumulator value in out machine
    """

    numberOfYesAnswers = 0
    ourMachine = Machine()

    while True:

        currentCommand = commandList[ourMachine.instructionPosition]
        #print(f"currentCommand: {currentCommand}")
        if ourMachine.instructionPosition in ourMachine.instructionHistory:
            return (ourMachine.instructionPosition - 1, commandList[ourMachine.instructionPosition - 1], ourMachine.accumulator)
        else:
            ourMachine.instructionHistory.add(ourMachine.instructionPosition)

        ourMachine.proccesCommand(currentCommand[0], currentCommand[1])


def breakInfiniteLoop(commandList):
    """
    Find command before the infinite loop starts.
    :param commandList: List of dictionaries that represent passport
    :return: command before the infinite loop,  its index and accumulator value in out machine
    """

    numberOfYesAnswers = 0
    ourMachine = Machine()

    while True:

        if ourMachine.instructionPosition == len(commandList):
            return ourMachine.accumulator

        currentCommand = commandList[ourMachine.instructionPosition]
        #print(f"currentCommand: {currentCommand}")
        if ourMachine.instructionPosition in ourMachine.instructionHistory:
            return False
        else:
            ourMachine.instructionHistory.add(ourMachine.instructionPosition)

        ourMachine.proccesCommand(currentCommand[0], currentCommand[1])

def fixInfiniteLoop(commandList):
    """
    Find which command we need to change so that infinite loop doesn't happen.
    :param commandList: List of dictionaries that represent passport
    :return: value ourMachine.accumulator of fixed instructions
    """

    for index, command in enumerate(commandList):
        successOrFail = False
        if command[0] == "nop":
            tempCommandList = copy.deepcopy(commandList)
            tempCommandList[index] = ("jmp", command[1])
            successOrFail = breakInfiniteLoop(tempCommandList)
        elif command[0] == "jmp":
            tempCommandList = copy.deepcopy(commandList)
            tempCommandList[index] = ("nop", command[1])
            successOrFail = breakInfiniteLoop(tempCommandList)

        if successOrFail:
            return successOrFail



if __name__ == "__main__":

    commandList = parseCommands("input.txt")
    print(f"commandList: {commandList}")

    commandBeforeRepetition = findInfiniteLoop(commandList)
    print(f"Part 1: {commandBeforeRepetition}")

    accumulator = fixInfiniteLoop(commandList)
    print(f"Part 2: {accumulator}")

