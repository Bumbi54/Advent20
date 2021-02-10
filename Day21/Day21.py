from collections import Counter
import copy
from bidict import bidict

def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a dictinary
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    inputDict = {}
    foods = set()
    foodCount = Counter()


    with open(fileName, 'r') as file:
        fileList = file.readlines()


    for line in fileList:
        ingredients, allergens = line.split(" (contains ")

        ingredients = set(ingredients.split(" "))
        foodCount.update(ingredients)
        foods = foods.union(ingredients)
        for allergen in allergens[:-2].split(", "):
            inputDict[allergen] = inputDict.get(allergen, ingredients).intersection(ingredients)

    return foods, inputDict, foodCount

def partOne(foods, inputDict):
    """
    Find food that do not contain allergens. I assume here that all of the foods in "inputDict" will have some allergen.
    :param foods: all of the foods
    :param inputDict: mapping of food with potential allergen
    :return:
    """

    allergenFood = set()
    for foodSet in inputDict.values():
        allergenFood = allergenFood.union(foodSet)

    return foods - allergenFood

def partTwo(inputDict):
    """
    Find allergen -> ingredients mapping
    :param inputDict: mapping of food with potential allergen
    :return:
    """

    print(inputDict)
    resolverMaping = copy.deepcopy(inputDict)
    foodMapping = bidict({})

    while resolverMaping:

        tempResolverMaping = {}
        for allergen, ingredients in resolverMaping.items():
            if len(ingredients) == 1:
                foodMapping[ingredients.pop()] = allergen
            else:
                tempResolverMaping[allergen] = ingredients.copy()
                for ingredient in ingredients:

                    if ingredient in foodMapping.keys():
                        tempResolverMaping[allergen].remove(ingredient)

        resolverMaping = tempResolverMaping

    return foodMapping

if __name__ == "__main__":

    foods, inputDict, foodCount = readInput("input.txt")
    print(f"inputDict: {inputDict}, foods: {foods}")

    print(f"inputDict: {inputDict}")
    noAllergenFood = partOne(foods, inputDict)

    count = 0
    for food in noAllergenFood:
        count += foodCount[food]

    print(f"Part 1: {count}")

    foodMapping = partTwo(inputDict)
    print(foodMapping)
    sortedAllergen  = list(foodMapping.values())
    sortedAllergen.sort()

    result = ""
    print(f"sortedAllergen: {sortedAllergen}")
    for allergen in sortedAllergen:
        result += foodMapping.inverse[allergen] + ","

    print(f"Part 2: {result[:-1]}")
