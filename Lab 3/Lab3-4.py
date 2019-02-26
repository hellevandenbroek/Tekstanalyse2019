import tweepy
from nltk import word_tokenize
from nltk.corpus import stopwords


def readFromFile():
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    names = []
    for line in f.readlines():
        tweeter = line
        name = tweeter[0:tweeter.index(":")]
        names.append(name)
        tweeter = line.split(',')
        tweets.append(tweeter[tweeter.index(":") + 1:])
    return tweets, names


results = readFromFile()
tweets = results[0]
names = results[1]


print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])
