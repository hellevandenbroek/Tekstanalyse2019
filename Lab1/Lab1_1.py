#!/usr/bin/env python3

import nltk
from collections import Counter

# These are variables, saves as strings

MALE = 'male'
FEMALE = 'female'
UNKNOWN = 'unknown'
BOTH = 'both'

# A set of words
MALE_WORDS = {'guy', 'spokesman', 'chairman', "men's", 'men', 'him', "he's", 'his', 'boy', 'boyfriend', 'boyfriends',
              'boys', 'brother', 'brothers', 'dad', 'dads', 'dude', 'father', 'fathers', 'fiance', 'gentleman',
              'gentlemen', 'god', 'grandfather', 'grandpa', 'grandson', 'groom', 'he', 'himself', 'husband', 'husbands',
              'king', 'male', 'man', 'mr', 'nephew', 'nephews', 'priest', 'prince', 'son', 'sons', 'uncle', 'uncles',
              'waiter', 'widower', 'widowers'}

# Another set of words
FEMALE_WORDS = {'heroine', 'spokeswoman', 'chairwoman', "women's", 'actress', 'women', "she's", 'her', 'aunt', 'aunts',
                'bride', 'daughter', 'daughters', 'female', 'fiancee', 'girl', 'girlfriend', 'girlfriends', 'girls',
                'goddess', 'granddaughter', 'grandma', 'grandmother', 'herself', 'ladies', 'lady', 'lady', 'mom',
                'moms', 'mother', 'mothers', 'mrs', 'ms', 'niece', 'nieces', 'priestess', 'princess', 'queens', 'she',
                'sister', 'sisters', 'waitress', 'widow', 'widows', 'wife', 'wives', 'woman'}


# A function that takes in "words"
def genderize(words):
    # finds out how many words are in the male_words set and female_words set
    mwlen = len(MALE_WORDS.intersection(words))
    fwlen = len(FEMALE_WORDS.intersection(words))

    # If it only intersects with one of the genders and not the other, it is set to be that gender.
    # Intersects with both: Both. Else (none): Unknown
    if mwlen > 0 and fwlen == 0:
        return MALE
    elif mwlen == 0 and fwlen > 0:
        return FEMALE
    elif mwlen > 0 and fwlen > 0:
        return BOTH
    else:
        return UNKNOWN


# Function that takes in "sentences"
def count_gender(sentences):
    # Counter modules are made
    sents = Counter()
    words = Counter()

    # Calling the genderize function on sentences
    # Incrementing sents (with 1) and words (with length of sentence a.k.a amount of words)
    for sentence in sentences:
        gender = genderize(sentence)
        sents[gender] += 1
        words[gender] += len(sentence)

    return sents, words

# Function taking in a text
def parse_gender(text):
    # List that makes all words in sentences in text lowercase and tokenizes them using nlkt
    sentences = [
        [word.lower() for word in nltk.word_tokenize(sentence)]
        for sentence in nltk.sent_tokenize(text)
        ]

    # Make new variables for sents and words and count the sentences vi have tokenized etc.
    sents, words = count_gender(sentences)

    total = sum(words.values())

    # Finding percent of count
    for gender, count in words.items():
        pcent = (count / total) * 100
        nsents = sents[gender]
        print(
            "{:0.3f}% {} ({} sentences)".format(pcent, gender, nsents)
        )



if __name__ == '__main__':
    with open('sample.txt', 'r') as f:
        parse_gender(f.read())
