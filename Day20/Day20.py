
import re
import numpy

def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    tileDict = {}
    coreTileDict = {}
    borderDict = {}
    reTitle = re.compile("Tile (\d+):")
    with open(fileName, 'r') as file:
        currentTile = 0
        for line in file:

            m = reTitle.findall(line)
            if m:
                currentTile = m[0]

                tileDict[currentTile] = []
                borderDict[currentTile] = []
            elif line == "\n":
                continue
            else:
                tileDict[currentTile].append(line.strip())


        for key, value in tileDict.items():
            borderDict[key].append(value[0])
            borderDict[key].append(value[-1])
            borderDict[key].append(value[0][::-1])
            borderDict[key].append(value[-1][::-1])

            coreTileDict[key] = []
            for line in value[1:-1]:
                coreTileDict[key].append(line[1:-1])

            leftBorder = ""
            rightVorder = ""

            for tileLine in value:
                leftBorder += tileLine[0]
                rightVorder += tileLine[-1]

            borderDict[key].append(leftBorder)
            borderDict[key].append(rightVorder)
            borderDict[key].append(leftBorder[::-1])
            borderDict[key].append(rightVorder[::-1])

        print(f"coreTileDict: {coreTileDict}")
        return tileDict, borderDict

def cornerTiles(borderDict):
    """
    Find which tiles are in corner
    :param borderDict: list of all possible borders for each tile
    :return:
    """

    edgeList = {}
    for tile, borders in borderDict.items():
        edgeList[tile] = []

        for border in borders:
            count = 0
            for otherTile, otherBorders in borderDict.items():

                if otherTile != tile and border in otherBorders:
                    count += 1

            edgeList[tile].append(count)


    return edgeList

if __name__ == "__main__":

    tileDict, borderDict = readInput("input.txt")
    print(f"tileDict: {tileDict}")
    print(f"borderDict: {borderDict}")

    edgeList = cornerTiles(borderDict)

    print(f"edgeList: {edgeList}")
    partOneResult = 1
    for key, value in edgeList.items():
        print(f" tile: {key}")
        print(f" sum: {sum(value)}")

        if sum(value) == 4:
            partOneResult *= int(key)

    print(f"partOneResult: {partOneResult}")