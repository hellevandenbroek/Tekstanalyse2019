from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer

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

def vectorize():
    corpus = ["This is very strange",
              "This is very nice"]
    vectorizer = TfidfVectorizer(min_df=1)
    X = vectorizer.fit_transform(corpus)
    idf = vectorizer.idf_
    print(dict(zip(vectorizer.get_feature_names(), idf)))


results = readFromFile()
tweets = results[0]
names = results[1]

print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

vectorize(tweets)
