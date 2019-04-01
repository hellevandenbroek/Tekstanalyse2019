from textblob import TextBlob
from keras.layers.embeddings import Embedding
from keras.models import load_model, Sequential
from keras.layers import Dense, Dropout, Activation, LSTM
from sklearn.model_selection import cross_val_score
import os
import time
import numpy as np
from functools import wraps
from sklearn.externals import joblib
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from keras.models import Sequential
from keras.wrappers.scikit_learn import KerasClassifier
from keras.layers import Dense, Dropout, Activation, LSTM
from sklearn.feature_extraction.text import TfidfVectorizer
import json
from transformer import TextNormalizer, GensimDoc2Vectorizer


# Source: https://keras.io/getting-started/sequential-model-guide/
# Source: https://medium.freecodecamp.org/how-to-build-a-twitter-sentiments-analyzer-in-python-using-textblob-948e1e8aae14
# Source: https://github.com/foxbook/atap/blob/master/snippets/ch12/deep_snark.py

def read_from_file():
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    for line in f.readlines():
        tweet = line
        tweets.append(tweet)
    return tweets


def analyse_sentiments(tweets):
    for tweet in tweets:
        sentiment = check_sentiment(tweet)
        save_sentimented_tweet(tweet, sentiment)


def check_sentiment(tweet):
    analyse = TextBlob(tweet).sentiment.polarity
    print('Tweet: {} ~~~Sentiments for tweet: {} \n'.format(tweet, analyse))
    #These are positive
    if analyse > 0:
        return 1
    #These are negative
    elif analyse < 0:
        return -1
    #These are neutral
    else:
        return 0


def save_sentimented_tweet(tweet, sent_value):
    """
    These are json objects used in the model.
    :param tweet:
    :param sent_value:
    """
    try:
        f = open("sentimentedTweets.txt", "a", encoding="utf-8")
        data = {"tweet": tweet, "sentimental_value": sent_value}
        json_data = json.dumps(data)
        f.write(json_data)
    finally:
        f.close()


def read_sentimented_tweets():
    f = open("sentimentedTweets.txt", "r", encoding="utf-8")

    # {"tweet": The Republican Party will become “The Party of Healthcare!”, "sentiment": 1}

    tweets = []
    for line in f.readlines():
        tweet = json.loads(line)
        tweets.append(tweet)
    return tweets


def create_model():
    model = Sequential()
    model.add(Dense(500, activation='relu', input_shape=(10000,)))
    model.add(Dense(150, activation='relu'))
    model.add(Dense(2, activation='softmax'))
    model.compile(
        loss='categorical_crossentropy',
        optimizer='adam',
        metrics=['accuracy']
    )
    return model


def train_model(path, model, cv):
    """
    Trains model from corpus at specified path;
    fitting the model on the full data and
    Returns the scores.
    """
    corpus = read_sentimented_tweets()

    X = list(corpus.sent_value)
    y = np.digitize(list(corpus.scores()), [0.0, 3.0, 5.1])
    scores = cross_val_score(model, X, y, cv=cv, scoring='accuracy')
    # Fit the model on entire data set
    model.fit(X, y)
    return scores

allTweets = read_from_file()
#analyseSentiment(allTweets)
print(create_model())

path = '../review_corpus_proc'
pipeline = Pipeline([
    ('norm', TextNormalizer()),
    ('vect', TfidfVectorizer(max_features=10000)),  # need to control feature count
    ('nn', KerasClassifier(build_fn=create_model,  # pass but don't call the function!
                           epochs=200,
                           batch_size=128))
])

train_model(path, pipeline, cv=12)

