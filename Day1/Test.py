
import timeit


def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            fileContent.append(int(line.strip()))

        return sorted(fileContent)

def findTwoEntriesWithSumSpecificSum(expenseList, targetedSum):
    """
    In list of expenses find two whose sum is equal to function input "targetedSum".
    :param expenseList: list of integeres that will be check
    :param targetedSum: value that sum of two expenses need to give
    :return:
    """
    for firstExpense in expenseList:
        for secondExpense in reversed(expenseList):

            if (firstExpense + secondExpense) > targetedSum:
                break

            if (firstExpense + secondExpense) == targetedSum:
                continue

def findThreeEntriesWithSumSpecificSum(expenseList, targetedSum):
    """
    In list of expenses find three whose sum is equal to function input "targetedSum".
    :param expenseList: list of integeres that will be check
    :param targetedSum: value that sum of three expenses need to give
    :return:
    """
    for firstExpense in expenseList:
        for secondExpense in expenseList:
            if (firstExpense + secondExpense) < targetedSum:
                for thirdExpense in expenseList:

                    if (firstExpense + secondExpense + thirdExpense) == targetedSum:
                        continue

def main():

    expenseList = readInput("input.txt")

    twoExpenses = findTwoEntriesWithSumSpecificSum(expenseList, 2020)

    threeExpenses = findThreeEntriesWithSumSpecificSum(expenseList, 2020)



if __name__ == "__main__":
    print(timeit.timeit('main()', setup='from __main__ import main', number=10))
