

def readInput(fileName):
    """
    Read input file and parse it into a list
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:

        fileContent = []
        for line in file:
            line = line.replace("F", "0")
            line = line.replace("B", "1")
            line = line.replace("R", "1")
            line = line.replace("L", "0")
            fileContent.append(int(line.strip(), 2))

        return fileContent

if __name__ == "__main__":

    seatingList = readInput("input.txt")
    print(f"seatingList: {seatingList}")

    print(f"Part 1: {max(seatingList)}")

    for number in range(max(seatingList)):

        if number not in seatingList:
            print(f"Potential part 2: {number}")
