from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

def readFromFile():
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    names = []
    for line in f.readlines():
        tweeter = line
        colon = tweeter.index(":")
        name = tweeter[0:colon]
        names.append(name)
        tweeter = line.split('-,-')
        tweets.append(tweeter[colon + 1:])
    return tweets, names


def count_vectorizer(account, comp_tweet):
    print("account", account)
    list_tweets = [tweet for tweet in account]
    list_tweets.append(comp_tweet)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_tweets)
    return X.toarray()


def compare(matrix):
    # TODO calculate similarity
    # euc_dist is in the nevner
    return euclidean_distances(matrix)
    # sum av alle vektorer / distansen


def compute_similarity(account, new_tweet):
    matrix = [account, new_tweet]
    vecs = [sum(account), sum(new_tweet)]
    comp = compare(matrix)
    print("vecs", vecs)
    print("comp", comp[0][1])
    return "lol"


def remove_stops(tokenized_tweets):
    all_stops = set(stopwords.words("english"))
    without_stops = []
    stops = []

    for word in tokenized_tweets:
        if word.lower() not in all_stops:
            without_stops.append(word)
        else:
            stops.append(word)
    return without_stops, stops




input_tweet = "this is a great wall and the animals are doing perfectly fine reportingly vegan peta vegetarian good!"
results = readFromFile()
tweets = results[0]
names = results[1]

print('\n---------------TWEETS---------------')
print("tweets:", tweets)
print('Input tweet: ', input_tweet)

print('\n---------------CORPORA---------------')
print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

print('\n---------------VECTORS---------------')
vectorized = count_vectorizer(tweets[0], input_tweet)

# sim = compute_similarity(vectorized[0], vectorized[1])


# vectorized2 = count_vectorizer(tweets[1], input_tweet)
print(vectorized)


print('\n---------------COMPARED---------------')
compared = compare(vectorized)
# compared2 = compare(vectorized2)


print('\n---------------CREDITS---------------')
print("Helle van den Broek - Author")
print("Truls Andreas Berglund - Author")
