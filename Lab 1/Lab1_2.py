#!/usr/bin/env python3

from nltk.book import *

# ex 2.a
def twoa():
    index = (text9.index('sunset'))
    print("The index of this word is: ", index)
    print_sentence(index)

# ex 2.b
def twob(word):
    indexes = [i for i, x in enumerate(text9) if x == word]
    print('The word occurs on indices: ', indexes)

    for i in indexes:
        print_sentence(i)

#finds the nearest dots on both sides of the word to find start and end of sentence
def print_sentence(index):
    startindex = 0
    endindex = len(text9)

    for i in range(index, endindex):
        if text9[i] == '.':
            endindex = i + 1
            break

    for i in range(index, startindex, -1):
        if text9[i] == '.':
            startindex = i + 1
            break

    print("The index of the start and end in this sentence are: ", startindex, endindex)
    print(text9[startindex:endindex])


if __name__ == '__main__':
    twoa()
    twob("sunset")
