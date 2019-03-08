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

def find_probability(ngram, word, context):
    #return ngram.probdi(word, context)
    return 'hello'

def start_gram(tweets):
    sentence = tweets
    n = 6
    sixgrams = ngrams(sentence.split(), n)
    for grams in sixgrams:
        print(grams)

tweets = readFromFile()[0]
print(tweets)
list_tweets = ''.join(str(e) for e in tweets)
print(list_tweets)
ng = start_gram(list_tweets)


