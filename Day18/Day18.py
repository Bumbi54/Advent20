import ast
import operator as op

# supported operators
operatorsPartOne = {ast.Add: op.add, ast.Sub: op.mul, ast.Mult: op.mul}
operatorsPartTwo = {ast.Mult: op.add, ast.Sub: op.mul}

def readInput(fileName):
    """
    Read input file and parse it into a string
    :param fileName: name of input file
    :return: list of input file content (each line is new element)
    """
    with open(fileName, 'r') as file:
        fileContent = file.readlines()

    return fileContent

def partOne(expr):
    """
    Resolve expression using ast and manual parsing of operations.
    """
    return executeMathPartOne(ast.parse(expr, mode='eval').body)

def executeMathPartOne(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operatorsPartOne[type(node.op)](executeMathPartOne(node.left), executeMathPartOne(node.right))
    else:
        raise TypeError(node)

def partTwo(expr):
    """
    Resolve expression using ast and manual parsing of operations.
    """
    return executeMathPartTwo(ast.parse(expr, mode='eval').body)

def executeMathPartTwo(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        return operatorsPartTwo[type(node.op)](executeMathPartTwo(node.left), executeMathPartTwo(node.right))
    else:
        raise TypeError(node)

if __name__ == "__main__":

    fileContent = readInput("input.txt")

    resultingList = []
    for line in fileContent:

        result = partOne(line.strip().replace("*", "-"))
        resultingList.append(result)

    print(f"Part one: {sum(resultingList)}")

    resultingList = []
    for line in fileContent:

        result = partTwo(line.strip().replace("*", "-").replace("+", "*"))
        resultingList.append(result)

    print(f"Part two: {sum(resultingList)}")