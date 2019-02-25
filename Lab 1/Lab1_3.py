import tweepy
from nltk import word_tokenize
from nltk.corpus import stopwords

consumer_key = "Z7b3xeY5P9nMSK9W3XU1Qqkca"
consumer_secret = "TZbRe2zyXFCAvr8LJ9M1SY4Y2WUehZiExHvh5keUKsW5jqPUi5"
access_key = "177320651-sChpCQ3UCq3sFcwYIOEmmpnl4yPG2LpZ8PYdDI4J"
access_secret = "fpOP5KHIvQFTtCVPnDhVZqqA1hP7E7Ptn5zHO8eR02Z9B"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
screen_name = 'twitter'
count = 10
tweet_mode = 'extended'

string = api.user_timeline(screen_name=screen_name,count=count,tweet_mode=tweet_mode)
tweets = [tweet.full_text for tweet in string]


def removeStops(tokenized_tweets):
    all_stops = set(stopwords.words("english"))
    without_stops = []
    stops = []

    for word in tokenized_tweets:
        if word.lower() not in all_stops:
            without_stops.append(word)
        else:
            stops.append(word)
    return without_stops, stops

def tokenize(tweets):
    tokens = []
    for tweet in tweets:
        tokens += word_tokenize(tweet)
    return set(tokens)

#Tokenizing tweets
tokenized_tweets=(tokenize(tweets))

#Removing stopwords:
result_stops = removeStops(tokenized_tweets)

print('\n---------------TOKENIZING---------------')
print('All tweets: {}'.format(tweets))
print('Tokenized tweets: {}'.format(tokenized_tweets))
print('\n---------------STOPWORDS---------------')
print('Stopwords removed: {}'.format(result_stops[1]))
print('The words without stops: {}'.format(result_stops[0]))
