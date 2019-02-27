from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

def readFromFile():
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


def count_vectorizer(corpus, comparing):
    list_tweets = [tweet for tweet in corpus]
    list_tweets.append(comparing)
    print(list_tweets)
    #for tweet in corpus:
        #list_tweets.append(' '.join(tweet))
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_tweets)
    return X.toarray()

def compare_tweet_corpus(tweet, matrix):
    vectorizer = CountVectorizer()
    Y = vectorizer.fit_transform([tweet])
    print(euclidean_distances(tweet, matrix))

def compare(matrix):
    print(matrix)
    return euclidean_distances(matrix)


input_tweet = "this is a great wall and the animals are doing perfectly fine reportingly good!"
results = readFromFile()
tweets = results[0]
names = results[1]

print('\n---------------TWEETS---------------')
print("tweets:", tweets)

print('\n---------------CORPORA---------------')
print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

print('\n---------------VECTORS---------------')
vectorized = count_vectorizer(tweets[0], input_tweet)
vectorized2 = count_vectorizer(tweets[1], input_tweet)

compared = compare(vectorized)
compared2 = compare(vectorized2)
print(vectorized)
print(vectorized2)

print('\n---------------COMPARED---------------')

print(compared)


print('******************************')
print('Tweet: ', input_tweet)
