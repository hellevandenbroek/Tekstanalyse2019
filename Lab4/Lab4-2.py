from nltk import ngrams



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
        tweeter = line.split('-,-')
        tweets.append(tweeter[colon + 1:])
    return tweets, names


def split_tweets(tweets):
    list_tweets = []
    for line in tweets:
        for word in line.split():
            list_tweets.append(word)
    return list_tweets


def start_ngram():
    tweets = readFromFile()[0][0]  # tweets > trump's
    print(tweets)
    spl = split_tweets(tweets)
    model = ngrams(spl, 3)

    prob = find_probability(model, "and", tweets)
    print(prob)
    return model


def find_probability(ngram, word, context):
    return ngram.probdi(word, context)


ng = start_ngram()

