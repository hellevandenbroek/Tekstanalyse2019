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

#write code to tokenize tweets
tokens = []
for tweet in tweets:
    tokens += word_tokenize(tweet)
tokenized = set(tokens)

#remove english stopwords
stopwords = set(stopwords.words("english"))

without_stops = []

for word in tokenized:
    if word.lower() not in stopwords:
        without_stops.append(word)

print(without_stops)

