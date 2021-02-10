
import re


def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    passwordPolicyList = []
    reMatch = re.compile("(\d+)-(\d+) (\w): (\w+)")

    with open(fileName, 'r') as file:
        fileList = file.readlines()

    for passwordPolicy in fileList:
        m = reMatch.findall(passwordPolicy)
        passwordPolicyList.append(m[0])

    return passwordPolicyList



def checkPasswordsPartOne(passwordPolicyList):
    """
    In list of passwords check which are valid by their password policy. Part one policy.
    :param passwordPolicyList: list of passwords and their policies
    :return:
    """
    validPasswords = []
    for passwordPolicy in passwordPolicyList:

        letterCount = int(passwordPolicy[3].count(passwordPolicy[2]))
        lowCount = int(passwordPolicy[0])
        highCount = int(passwordPolicy[1])

        if lowCount <= letterCount <= highCount:

            validPasswords.append(passwordPolicy)

    return validPasswords

def checkPasswordsPartTwo(passwordPolicyList):
    """
    In list of passwords check which are valid by their password policy. Part two policy.
    :param passwordPolicyList: list of passwords and their policies
    :return:
    """
    validPasswords = []
    for passwordPolicy in passwordPolicyList:

        password = passwordPolicy[3]
        targtedChar = passwordPolicy[2]
        firstPosition = int(passwordPolicy[0])
        secondPosition = int(passwordPolicy[1])

        if  (targtedChar == password[firstPosition - 1]) ^ (targtedChar == password[secondPosition - 1]):
            validPasswords.append(passwordPolicy)

    return validPasswords

if __name__ == "__main__":

    passwordPolicyList = readInput("input.txt")
    print(f"passwordPolicyList: {passwordPolicyList}")

    validPasswords = checkPasswordsPartOne(passwordPolicyList)
    print(f"Part 1: {len(validPasswords)}")

    validPasswords = checkPasswordsPartTwo(passwordPolicyList)
    print(f"Part 2: {len(validPasswords)}")
