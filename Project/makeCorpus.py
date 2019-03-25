import tweepy

def make_corpus(username):
    consumer_key = "LqZEmCpMMaHS6fgxr4J0OVawP"
    consumer_secret = "HeTmwvVd0NDFrdvz9j4uNNhNFYhA7rrBKMSE6MxkS5DnVx4VKH"
    access_key = "788662964-bBmuNBWLuK6opUT3HyJVtVw5y9WfOHLe1CtB45LT"
    access_secret = "yhqFB8Izpfb6w3pUBxPBUKj62pY654F5cUhTbyCYYRAea"
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweet_mode = 'extended'
    string = api.user_timeline(screen_name=username, tweet_mode=tweet_mode)
    tweets = [tweet.full_text for tweet in string]
    save_to_file(tweets)

def save_to_file(tweets):
    try:
        f = open("test.txt", "ab")
        top_tweets = tweets
        for tweet in top_tweets:
            if len(tweet) > 1:
                f.write(tweet.encode() + '\n'.encode())
    finally:
        f.close()
