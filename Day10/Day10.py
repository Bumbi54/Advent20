
import numpy as np
import networkx as nx

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

        return fileContent

def findVoltage(adaptersList):
    """
    Find difference in voltage from 0 to outlet by using adapters
    :param adaptersList: sorted list of adapters voltages
    :return:
    """

    startList = [0] + adaptersList[:]
    endList = adaptersList + [adaptersList[-1] + 3]

    return list(np.subtract(endList, startList))

def findAllAdapterCombinationsNx(adaptersList):
    """
    As expected. It doesn't work.
    Find number of possible combination of adapters.
    :param adaptersList: sorted list of adapters voltages
    :return:
    """

    extendedAdaptersList = [0] + adaptersList[:] + [adaptersList[-1] + 3]

    G = nx.DiGraph()
    G.add_nodes_from(extendedAdaptersList)

    for index, originAdapter in enumerate(extendedAdaptersList):
        print(f"originAdapter: {originAdapter}")
        print(f"index: {index}")
        for endAdapter in extendedAdaptersList[index + 1 : index + 4]:
            print(f"    endAdapter: {endAdapter}")

            if endAdapter - originAdapter < 4:
                G.add_edge(originAdapter, endAdapter)

    print(len(list(nx.all_simple_paths(G, 0, extendedAdaptersList[-1]))))

def findAllAdapterCombinations(adaptersList):
    """
    Find number of possible combination of adapters.
    :param adaptersList: sorted list of adapters voltages
    :return:
    """
    extendedAdaptersList = [0] + adaptersList[:] + [adaptersList[-1] + 3]
    historyOfPaths = dict.fromkeys(extendedAdaptersList, 0)
    historyOfPaths[0] = 1
    #print(extendedAdaptersList)

    for index, originAdapter in enumerate(extendedAdaptersList):
        #print(f"originAdapter: {originAdapter}")
        #print(f"index: {index}")
        for endAdapter in extendedAdaptersList[index + 1 : index + 4]:

            #print(f"    endAdapter: {endAdapter}")
            if endAdapter - originAdapter < 4:
                historyOfPaths[endAdapter] += historyOfPaths[originAdapter]
        #print(f"    historyOfPaths: {historyOfPaths}")

    return historyOfPaths[adaptersList[-1] + 3]




if __name__ == "__main__":

    adaptersList = readInput("input.txt")
    print(f"adaptersList: {adaptersList}")

    #voltageList = findVoltage(sorted(adaptersList))
    #print(f"Part 1. Count 1: {voltageList.count(1)}, Count 3: {voltageList.count(3)}, Result: {voltageList.count(1) * voltageList.count(3)}")

    adapterCombinations = findAllAdapterCombinations(sorted(adaptersList))
    print(f"Part 2: {adapterCombinations}")
