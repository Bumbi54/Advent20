
import re
import json
import ast

def parsePassports(fileName):
    """
    Read input file and parse it list of dictionaries
    :param fileName: name of input file
    :return: list passport saved as dictinaries
    """

    passportList = []
    with open(fileName, 'r') as file:
        fileString = file.read()

    unparsedPasspoertList = fileString.split("\n\n")

    for unparsedPassport in unparsedPasspoertList:

        stringPassport = re.split(' |\n',unparsedPassport)

        passport = {}

        for field in stringPassport:
            key, value = field.split(":")
            passport[key] = value

        passportList.append(passport)

    return passportList

def checkValidPasswords(passportList):
    """
    Find passwords that are valid
    :param passportList: List of dictionaries that represent passport
    :return: list of valid passport
    """

    validPassportList = []

    for passport in passportList:

        fieldNames = passport.keys()
        if (len(fieldNames)) > 7 or (len(fieldNames) > 6 and  "cid" not in fieldNames):
            validPassportList.append(passport)


    return validPassportList


def checkValidPasswordsPartTwo(passportList):
    """
    Find passwords that are valid with more strict rules
    :param passportList: List of dictionaries that represent passport
    :return: list of valid passport
    """

    validPassportList = []
    hexaPattern = re.compile(r'^#([0-9a-f]){6}$')
    numberPattern = re.compile(r'^([0-9]){9}$')

    for passport in passportList:

        fieldNames = passport.keys()
        if (len(fieldNames)) > 7 or (len(fieldNames) > 6 and  "cid" not in fieldNames):

            valid = True

            valid &= 1920 <= int(passport["byr"]) <= 2002
            #print("Condition: %s, Valid: %s" % ("byr", valid))
            valid &= 2010 <= int(passport["iyr"]) <= 2020
            #print("Condition: %s, Valid: %s" % ("iyr", valid))
            valid &= 2020 <= int(passport["eyr"]) <= 2030
            #print("Condition: %s, Valid: %s" % ("eyr", valid))

            if "cm" in  passport["hgt"]:
                valid &= 150 <= int(passport["hgt"].replace("cm", '')) <= 193
            elif "in" in  passport["hgt"]:
                valid &= 59 <= int(passport["hgt"].replace("in", '')) <= 76
            else:
                valid = False

            #print("Condition: %s, Valid: %s" % ("hgt", valid))

            m = re.search(hexaPattern, passport["hcl"])
            if not m:
                valid = False

            #print("Condition: %s, Valid: %s" % ("hcl", valid))

            valid &= passport["ecl"] in ["amb", "blu" ,"brn", "gry", "grn", "hzl", "oth"]

            #print("Condition: %s, Valid: %s" % ("ecl", valid))

            m = re.search(numberPattern, passport["pid"])
            if not m:
                valid = False

            #print("Condition: %s, Valid: %s" % ("pid", valid))

            if valid:
                validPassportList.append(passport)
            #print("############################################################")

    return validPassportList

if __name__ == "__main__":

    passportList = parsePassports("input.txt")
    print(f"passportList: {passportList}")
    print(f"len(passportList): {len(passportList)}")

    validPasswords = checkValidPasswords(passportList)
    print(f"Part 1: {len(validPasswords)}")

    validPasswords = checkValidPasswordsPartTwo(passportList)
    print(f"Part 2: {len(validPasswords)}")

