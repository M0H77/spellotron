"""
file: correction_methods.py
description: project
author: Mohammed Alhamadah
"""

from make_dict import *
AE = make_dict2("american-english.txt")
KL = make_dict("keyboard-letters.txt")
ALPHABET = tuple( chr( code ) for code in range( ord( "a" ), ord("z") + 1 ) )
PUNCTUATION =("-", "[" ,"]" ,"{", "}", "(",")","@","#","ˆ","&","," ,".","!","?",":",";","”","’","*","+","=","/")


def correct_adj(word):
    """
    this function takes an illegal word and try to fix it by changing each letter to its adjacents
     in the keyboard and then returns the fixed word, if couldn't be fixed, the original word is returned
    :param word: str
    :return: str
    """
    corrected = []
    # print (word)
    # old_word = word
    # while word not in AE:
    # word =old_word
    for i in range(len(word)):
        for key, val in KL.items():
            if word[i] == key:
                for j in range(len(val)):
                    temp = word
                    word = word[:i] + val[j] + word[i + 1:]
                    if word in AE:
                        # print(word)
                        corrected.append(word)
                        return word
                    else:
                        word = temp
    # print(word)
    return word

def correct_extra(word):
    """
    this function takes an illegal word and try to fix it by removing one letter from it each time
     and then returns the fixed word, if couldn't be fixed, the original word is returned
    :param word: str
    :return: str
    """
    old_word = word
    for i in range(len(word)):
        word = old_word
        word = word[:i] + word[i + 1:]
        if word in AE:
            # print(word)
            return word
        else:
            word = old_word
    # print(word)
    return word

def correct_missed(word):
    """
    this function takes an illegal word and try to fix it by trying to add all the alphabet
     letters at each possible index and then returns the fixed word, if couldn't be fixed,
      the original word is returned
    :param word: str
    :return: str
    """
    old_word = word
    for i in range(0,len(word)):
        for letter in range(0,len(ALPHABET)):
            word = old_word
            word = word[:i] + ALPHABET[letter] + word[i :]
            if word in AE:
                # print(word)
                return word
            else:
                word = old_word
    # print(word)
    return word