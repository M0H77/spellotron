"""
file: spellotron.py
description: project
author: Mohammed Alhamadah
"""

import sys
import re
import string
from correction_methods import *
from read_file import *
from make_dict import *


AE = make_dict2("american-english.txt")


def to_lst(text):
    """
    this function converts a string to a list
    :param text: str
    :return: lst
    """
    lst=[]
    text = text.split()
    for i in text:
        lst.append(i)
    return lst


def remove_punc(word):
    """
    this function remove punctuations from the start and end of a word (string)
    :param word: str
    :return: a tuple of str with no punctuations + a list of the removed punctuations
    """
    word1 = word.strip(string.punctuation)
    punc_lst = word.split(word1)
    return word1, punc_lst

def add_punc(word,punc):
    """
    this function adds punctuations that were removed from the start and end of a word (string) back.
    :param word: str
    :param punc: a list of the removed punctuations
    :return: str with punctuations
    """
    word = punc[0] + word + punc[1]
    return word


def if_uppercase(word):
    """
    this function changes the first letter of an illegal word to lowercase, If the word becomes
     legal ,it is returned, otherwise it will try to fix the word by the 3 correction methods and then returns
     the fixed word with the first letter capitalized, if couldn't be fixed, the original word is returned.
    :param word:
    :return:
    """
    word = str.lower(word)
    if word not in AE:
        checked_word = correct_adj(word)
        if checked_word != word:
            checked_word = checked_word[0].upper() + checked_word[1:]
            return checked_word
        else:
            checked_word = correct_missed(word)
            if checked_word != word:
                checked_word = checked_word[0].upper() + checked_word[1:]
                return checked_word
            else:
                checked_word = correct_extra(word)
                if checked_word != word:
                    checked_word = checked_word[0].upper() + checked_word[1:]
                    return checked_word
                else:
                    word = word[0].upper() + word[1:]
                    return word
    else:
        word = word[0].upper() + word[1:]
        return word




def correction_sequence(lst, mode):
    """
     this function does a sequence of corrections and checking to any illegal word found in the list provided.
     when an illegal word is found, it will be corrected using the first method (correct_adj) if could't be fixed,
     the second method (correct_extra) will be tried, if could't be fixed, the third method will be tried
     (correct_missed).then oen of two results that include an output (lines/words), the number of words read, the number
     of corrected words and a list of the them before correction, the number of unknown words and a list of them.
     words, will be printed based on a the argument the user enters. any number found in the list will be treated
     as a legal word and will be counted.
    :param lst: a list of words (string)
    :param mode: a string of the chosen mode.
    """
    uncorrected = []
    legal_words = []
    be_correction = []
    af_correction = []

    word_read = 0
    corrected = 0
    unknown = 0

    formatted_sentence =''

    for word in lst:
        punc_lst = []
        flag = 0
        word_read += 1
        if word.isdigit():
            legal_words.append(word)
            formatted_sentence += ' ' + word
        elif word == r"\n":
            formatted_sentence += "\n"         # add new line character
        elif re.fullmatch(r'\W+', word):
            formatted_sentence += ' ' + word
        else:
            if re.search(r'^\W|\W$', word):     # if a word has punctuations
                flag = 1
                word,punc_lst = remove_punc(word)   # remove punctuations
            if word not in AE:
                checked_word = correct_adj(word)
                if checked_word != word:
                    corrected += 1
                    if flag ==1:                       # if punctuations were removed add them back
                        word = add_punc(word,punc_lst)
                    be_correction.append(word)
                    if flag ==1:
                        checked_word = add_punc(checked_word, punc_lst)
                    af_correction.append(checked_word)
                    formatted_sentence += ' '+ checked_word
                else:
                    checked_word = correct_missed(word)
                    if checked_word != word:
                        corrected += 1
                        if flag == 1:
                            word = add_punc(word, punc_lst)
                        be_correction.append(word)
                        if flag == 1:
                            checked_word = add_punc(checked_word, punc_lst)
                        af_correction.append(checked_word)
                        formatted_sentence += ' '+ checked_word
                    else:
                        checked_word = correct_extra(word)
                        if checked_word != word:
                            corrected += 1
                            if flag == 1:
                                word = add_punc(word, punc_lst)
                            be_correction.append(word)
                            if flag == 1:
                                checked_word = add_punc(checked_word, punc_lst)
                            af_correction.append(checked_word)
                            formatted_sentence += ' '+ checked_word
                        elif word[0].isupper():
                                # print("yes")

                                checked_word =if_uppercase(word)  #if the first letter is capital call if_uppercase()
                                back_to_lower = str.lower(checked_word)
                                if back_to_lower in AE:
                                    if flag == 1:
                                        checked_word = add_punc(checked_word, punc_lst)
                                    legal_words.append(checked_word)
                                    formatted_sentence += ' ' + checked_word
                                elif checked_word != word:
                                    corrected += 1
                                    if flag == 1:
                                        word = add_punc(word, punc_lst)
                                    be_correction.append(word)
                                    if flag == 1:
                                        checked_word = add_punc(checked_word, punc_lst)
                                    af_correction.append(checked_word)
                                    formatted_sentence += ' ' + checked_word
                                else:
                                    if flag == 1:
                                        word = add_punc(word, punc_lst)
                                    unknown += 1
                                    uncorrected.append(word)
                                    formatted_sentence += ' ' + word

                        else:
                            if flag == 1:
                                word = add_punc(word, punc_lst)
                            unknown += 1
                            uncorrected.append(word)
                            formatted_sentence += ' '+ word
            else:
                if flag == 1:
                    word = add_punc(word, punc_lst)
                legal_words.append(word)
                formatted_sentence += ' '+ word
    # print(uncorrected)
    # print(legal_words)
    # print(be_correction)
    # print(af_correction)
    # print(word_read)
    # print(corrected)
    if mode == "words":
        for k in range(len(be_correction)):

            print(be_correction[k],"==>", af_correction[k])
    elif mode =="lines":
        print(formatted_sentence)

    print()
    print(word_read,"words read")
    print()
    print(corrected,"corrected words")
    print(be_correction)
    print()
    print(unknown, "unknown words")
    print(uncorrected)


def main():

    if len(sys.argv) == 3:
        f = convert_file(sys.argv[2])
        correction_sequence(f, sys.argv[1])
    else:
        if len(sys.argv) == 2 and sys.argv[1] == "words" or sys.argv[1] =="lines":
            while True:
                text = str(input("spellotron> "))
                if text == "":
                    break
                print()
                lst = to_lst(text)
                correction_sequence(lst, sys.argv[1])
        else:
            print("Usage: python3.7 spellotron.py words/lines [filename]")


main()
