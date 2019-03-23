from textblob import TextBlob

# Sources: https://medium.freecodecamp.org/how-to-build-a-twitter-sentiments-analyzer-in-python-using-textblob-948e1e8aae14


def readFromFile():
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    for line in f.readlines():
        tweet = line
        tweets.append(tweet)
    return tweets


all_tweets = readFromFile()

for tweet in all_tweets:
    print(tweet)
    analysis = TextBlob(tweet)
    print(analysis.sentiment)
    if analysis.sentiment[0] > 0:
        print('Positive')
    elif analysis.sentiment[0] < 0:
        print('Negative')
    else:
        print('Neutral')

        