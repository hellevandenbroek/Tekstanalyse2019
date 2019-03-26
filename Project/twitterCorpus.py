import tweepy
import pathlib


class CorpusGenerator:
    def __init__(self, twitter_user):
        consumer_key = "LqZEmCpMMaHS6fgxr4J0OVawP"
        consumer_secret = "HeTmwvVd0NDFrdvz9j4uNNhNFYhA7rrBKMSE6MxkS5DnVx4VKH"
        access_key = "788662964-bBmuNBWLuK6opUT3HyJVtVw5y9WfOHLe1CtB45LT"
        access_secret = "yhqFB8Izpfb6w3pUBxPBUKj62pY654F5cUhTbyCYYRAea"
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        pathlib.Path('Corpus').mkdir(exist_ok=True)

        self.api = tweepy.API(auth)
        self.tweet_mode = 'extended'
        self.username = twitter_user
        self.tweets = []
        self.add_tweets()

    def add_tweets(self):
        string = self.api.user_timeline(screen_name=self.username, tweet_mode=self.tweet_mode, count=200)
        self.tweets = [tweet.full_text for tweet in string]
        self.remove_unnecessary()

    def _is_sufficient_data(self):
        return len(self.tweets) > 160

    def save_to_file(self):
        if len(self.tweets) == 0:
            return

        if not self._is_sufficient_data():
            print("Not enough data to save. Please choose another account.")
            return

        try:
            file = open("Corpus/{}.txt".format(self.username.lower()), "wb")
            top_tweets = self.tweets
            for tweet in top_tweets:
                if len(tweet) > 1:
                    file.write(tweet.encode() + '\n'.encode())
        finally:
            file.close()
            print("Saved regular {} to corpus".format(self.username))

    def remove_unnecessary(self):
        newCorpus = []
        for tweet in self.tweets:
            newTweet = ""
            for word in tweet.split():
                if not self.is_unnecessary(word):
                    newTweet += word
                    newTweet += " "
            newCorpus.append(newTweet)
        self.tweets = newCorpus

    def is_unnecessary(self, word):
        if word.startswith('@') or word.startswith('RT') or word.startswith('http'):
            return True
        else:
            return False


if __name__ == '__main__':
    print("Started CorpusGenerator")
    corpus = CorpusGenerator()
