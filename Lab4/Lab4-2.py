from nltk import ngrams
import nltk

"""
    TODO: 
    - find out how to generate full sentence using nltk's ngrams
    - how ngram works
    http://www.nltk.org/_modules/nltk/model/ngram.html
    - feature for input 
    - return most correct sentence and its probability
"""


def readFromFile():
    # trying without SW
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    names = []
    for line in f.readlines():
        tweeter = line
        colon = tweeter.index(":")
        name = tweeter[0:colon]
        names.append(name)
        only_tweets = tweeter[colon + 1:]
        new_tweeter = only_tweets.split('-,-')
        for tw in new_tweeter:
            tweets.append(tw.lower())
    return tweets, names


def count_ngrams(ng, string):
    length = len(ng)
    print(ng)
    count = 0
    for gram in ng:
        if string in gram:
            count += 1
    prob = count/length
    return prob


def start_gram(tweets):
    n = 4
    complete_ngram = []
    ngram = ngrams(tweets.split(), n)
    for gram in ngram:
        complete_ngram.append(gram)
    return complete_ngram


print('\n---------------INPUT---------------')
string = 'america'
print(string)


print('\n---------------N-GRAM---------------')
tweets = readFromFile()[0]
list_tweets = ''.join(str(e) for e in tweets)
ng = start_gram(list_tweets)


print('\n---------------PROBABILITY FOR INPUT---------------')
prob = count_ngrams(ng, string)

print(prob)
