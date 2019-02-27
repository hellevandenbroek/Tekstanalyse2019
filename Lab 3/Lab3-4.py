from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer


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

def count_vectorizer(corpus):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(corpus)
    return(X.toarray())

results = readFromFile()
tweets = results[0]
names = results[1]

print('\n---------------CORPUSES---------------')
print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

print('\n---------------VECTORS1---------------')
print(count_vectorizer(tweets[0]))
print('\n---------------VECTORS2---------------')
print(count_vectorizer(tweets[1]))

# vectorize(tweets)
