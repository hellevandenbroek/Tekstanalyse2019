from keras.layers import Dense, Activation
from keras.models import Sequential
from textblob import TextBlob



# Sources: https://medium.freecodecamp.org/how-to-build-a-twitter-sentiments-analyzer-in-python-using-textblob-948e1e8aae14


def readFromFile():
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    for line in f.readlines():
        tweet = line
        tweets.append(tweet)
    return tweets


def analyseSentiment(tweets):
    for tweet in tweets:
        print(tweet)
        analysis = TextBlob(tweet)
        print(analysis.sentiment)
        if analysis.sentiment[0] > 0:
            print('Positive')
        elif analysis.sentiment[0] < 0:
            print('Negative')
        else:
            print('Neutral')

allTweets = readFromFile()
analyseSentiment(allTweets)

#Source https://keras.io/getting-started/sequential-model-guide/

model = Sequential()
model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])

print(allTweets)
