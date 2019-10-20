"""
file: make_dict.py
description: project
author: Mohammed Alhamadah
"""

def make_dict(filename):
    """
    this function converts a txt file to a dictionary with the first character in each
    line as the key and the rest of the line as the value
    :param filename: txt file
    :return: dict
    """
    KL = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split(" ")
            first_letter = line[0]
            adj = []
            for letter in line[1:]:
                adj.append(letter)
            KL[first_letter] = adj
    # for key in KL:
    #     print(key,"=",KL[key])
    return KL


def make_dict2(filename):
    """
    this function converts a txt file to a dictionary with the each line as the key and the value.
    :param filename: txt file
    :return: dict
    """
    AE = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line.split()
            for word in line:
                AE[word] = word
    # for key in KL:
    #     print(key,"=",KL[key])
    return AE