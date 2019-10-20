"""
file: read_file.py
description: project
author: Mohammed Alhamadah
"""
def convert_file(filename):
    """
    this function converts a txt file to a list.
    :param filename: txt file
    :return: lst
    """
    content =[]
    with open(filename) as f:
        for line in f:
            line = line.strip()
            line = line + " " + str(r"\n")
            line = line.split()
            for word in line:
                content.append(word)
    return content