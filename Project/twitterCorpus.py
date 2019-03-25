import tweepy


class CorpusGenerator():
    def __init__(self, twitter_user):
        consumer_key = "LqZEmCpMMaHS6fgxr4J0OVawP"
        consumer_secret = "HeTmwvVd0NDFrdvz9j4uNNhNFYhA7rrBKMSE6MxkS5DnVx4VKH"
        access_key = "788662964-bBmuNBWLuK6opUT3HyJVtVw5y9WfOHLe1CtB45LT"
        access_secret = "yhqFB8Izpfb6w3pUBxPBUKj62pY654F5cUhTbyCYYRAea"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        self.api = tweepy.API(auth)

        self.tweet_mode = 'extended'
        self.username = twitter_user
        self.tweets = []

    def add_tweets(self):
        string = self.api.user_timeline(screen_name=self.username, tweet_mode=self.tweet_mode, count=200)
        self.tweets = [tweet.full_text for tweet in string]


