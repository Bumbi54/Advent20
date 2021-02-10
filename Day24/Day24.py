
import time
from operator import add

def readInput(fileName):
    """
    Read input file, parse lines with regex and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    with open(fileName, 'r') as file:
        return file.read().splitlines()

def partOne(tileList):
    """
    Resolve tile positions. And find their color.
    :param tileList:
    :return:
    """

    blackTiles = set()
    directionsDict = {
                        "e" : (0, 1),
                        "se": (-0.5, 0.5),
                        "sw": (-0.5, -0.5),
                        "w": (0, -1),
                        "nw": (0.5, -0.5),
                        "ne": (0.5, 0.5),
                        }

    for tile in tileList:

        #print(f"tile: {tile}")
        index = 0
        currentPosition = (0, 0)
        while index < len(tile):

            direction = tile[index]

            if direction in ["s", "n"]:
                index += 1
                direction += tile[index]

            #print(f"Direction: {direction}")
            currentPosition = tuple(map(add, currentPosition, directionsDict[direction]))
            index += 1
        #print(f"currentPosition: {currentPosition}")
        if currentPosition in  blackTiles:
            blackTiles.remove(currentPosition)
        else:
            blackTiles.add(currentPosition)

    return blackTiles

def partTwo(tileDict):
    """
    Resolve color of tiles over 100 rounds.
    :param tileDict: set of coordinates that represent black tiles
    :return:
    """

    directionsDict = {
                        "e" : (0, 1),
                        "se": (-0.5, 0.5),
                        "sw": (-0.5, -0.5),
                        "w": (0, -1),
                        "nw": (0.5, -0.5),
                        "ne": (0.5, 0.5)
                        }

    for _ in range(100):
        tilesToCheck = set()

        for tile in tileDict:
            for direction in directionsDict.values():
                tilesToCheck.add(tuple(map(add, tile, direction )))
            tilesToCheck.add(tile)

        tempTileDict = set()

        #print(f"tilesToCheck: {tilesToCheck}")

        for tile in tilesToCheck:

            count = sum([1 for direction in directionsDict.values() if tuple(map(add, tile, direction)) in tileDict])
            if tile in tileDict:
                if count != 0 and count <= 2:
                    tempTileDict.add(tile)
            else:
                if count == 2:
                    tempTileDict.add(tile)

        tileDict = tempTileDict

    return tileDict


if __name__ == "__main__":

    tileList = readInput("input.txt")
    print(f"tileList: {tileList}")

    tileDict = partOne(tileList)
    print(f"Part 1: {len(tileDict)}")

    finalTileDict = partTwo(tileDict)
    print(f"Part 2: {len(finalTileDict)}")

    #validPasswords = checkPasswordsPartTwo(passwordPolicyList)
    #print(f"Part 2: {len(validPasswords)}")
