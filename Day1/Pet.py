#!/usr/local/bin/python3.8

"""
Advent of Code Day 1
"""

__author__ = "Kresimir Petrovic"
__version__ = "0.1.0"
__license__ = "MIT"

from itertools import permutations
import numpy as np
import timeit

debug = 0

def main():
    """ Main entry point of the app """


    file = load_input("input.txt")
    dataset = list(map(int, file))
    two = find_sum_any_perm(dataset, 2, 2020)


    three = find_sum_any_perm(dataset, 3, 2020)


def find_sum_any_perm(input, len, target):
    perms = permutations(input, len)
    for item in list(perms):
        if sum(item) == target:
            if debug == 1: print ("Found: ", item)
            return (item)


def load_input (filename):

    f = open (filename, "r")

    content = f.read().splitlines()
    return content


if __name__ == "__main__":
    """ This is executed when run from the command line """
    print(timeit.timeit('main()', setup='from __main__ import main', number=10))



