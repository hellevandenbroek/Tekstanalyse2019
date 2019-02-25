#!/usr/bin/env python3
import nltk
from nltk.corpus import brown as browncorpus

def four(corpus, occurrence, firstwords):

    sliceswords = []
    x = 0
    while x < firstwords:
        for w in corpus.words():
            w.lower()
            sliceswords.append(w)
            x += 1

    words = (nltk.FreqDist(sliceswords))

    match = [' ']
    for word in words:
        if words[word] >= occurrence:
            match.append(word)
    return match


occurrence = 300
firstwords = 3000


print(four(browncorpus, occurrence, firstwords))
