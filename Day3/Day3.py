
def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """

    with open(fileName, 'r') as file:
        return file.readlines()

def parseSlopeTrees(slopedMatrix):
    '''
    Parse trees into set as pair of coordinates.
    :param asteroidMatrix:
    :return:
    '''

    treesSet = set()
    maxRows = len(slopedMatrix)
    #don't forget newline
    maxColumns =len(slopedMatrix[0]) - 1

    for x, slopeLine in enumerate(slopedMatrix):
        for y, point in enumerate(slopeLine):

            if point == "#":
                treesSet.add((x,y))

    return (treesSet, maxRows, maxColumns)

def threesInPath(treesSet, maxRows, maxColumns, movementDirection):
    """
    Find how many trees are in our downward path.
    :param treesSet: set that contains trees coordinates.
    :param maxRows: number of rows in our dataset
    :param maxColumns: number of columns in our dataset
    :param movementDirection: tuple that contains increases on x/y
    :return: number of trees in our way.
    """

    currentCoordinate = [0, 0]
    treeCount = 0

    while currentCoordinate[0] < maxRows:
        #print(currentCoordinate)
        if tuple(currentCoordinate) in treesSet:
            treeCount += 1
        currentCoordinate[0] = (currentCoordinate[0] + movementDirection[0])
        currentCoordinate[1] = (currentCoordinate[1] + movementDirection[1]) % maxColumns

    return treeCount

if __name__ == "__main__":

    slopedMatrix = readInput("input.txt")
    (treesSet, maxRows, maxColumns) = parseSlopeTrees(slopedMatrix)
    print(f"maxRows: {maxRows}, maxColumns: {maxColumns}, treesSet: {treesSet}")

    treeCount = threesInPath(treesSet, maxRows, maxColumns, (1, 3))
    print(f"Part 1: {treeCount}")

    newDirections = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    treeCount = 1
    for direction in newDirections:
        treeCount *= threesInPath(treesSet, maxRows, maxColumns, direction)

    print(f"Part 2: {treeCount}")

