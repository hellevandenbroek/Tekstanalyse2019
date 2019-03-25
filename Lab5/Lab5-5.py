from textblob import TextBlob
from keras.layers.embeddings import Embedding
from keras.models import load_model, Sequential
from keras.layers import Dense, Dropout, Activation, LSTM

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
print(allTweets)

#Source https://keras.io/getting-started/sequential-model-guide/

model = Sequential()
model.add(Dense(10, input_dim=2, activation='relu', kernel_initializer='uniform'))
model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy'])
