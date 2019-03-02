from nltk import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

def readFromFile():
    # trying without SW
    f = open("twitterCorpusSW.txt", "r", encoding="utf-8")
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
    # Adding the account tweets to the list first,
    # then adding the input tweet last [-1]
    list_tweets = [tweet for tweet in account]
    list_tweets.append(comp_tweet)

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(list_tweets)
    return X.toarray()


def dist(matrix):
    euc = euclidean_distances(matrix)
    return euc


def compute_similarity(account, new_tweet):
    mean_value = 0

    for x in range(len(account)):
        line = account[x]
        dist_euc = dist([line, new_tweet])[1][0]
        calc_sum = 0

        for y in range(len(line)):
            calc_sum += line[y] * new_tweet[y]
        sim = (calc_sum / dist_euc)
        mean_value += sim
    mean_value /= len(account)
    return mean_value


def compare(first_acc, first_name, second_acc, second_name, input_tweet1):
    belongs_to = first_name
    not_to = second_name
    sim1 = compute_similarity(first_acc[:len(first_acc) - 1], first_acc[-1])
    sim2 = compute_similarity(second_acc[:len(second_acc) - 1], second_acc[-1])
    shortened_input = input_tweet1[:len(input_tweet1) // 2] + "..."

    if sim2 > sim1:
        belongs_to = second_name
        not_to = first_name

    print("similarity, {}:".format(first_name), sim1)
    print("similarity, {}:".format(second_name), sim2)
    print("The input tweet: '{}' seems to belong to {} rather than to {}".format(shortened_input, belongs_to, not_to))


input_tweet = "The great wall of China needs to be built quickly. We can no longer suffer the animals by not having the great wall of USA"
results = readFromFile()
tweets = results[0]
names = results[1]

'''
print('\n---------------TWEETS---------------')
print("tweets:", tweets)
print('Input tweet: ', input_tweet)
'''

print('\n---------------CORPORA---------------')
print(names[0], ': ', tweets[0])
print(names[1], ': ', tweets[1])

# ---------------VECTORS---------------'
first_account = count_vectorizer(tweets[0], input_tweet)
second_account = count_vectorizer(tweets[1], input_tweet)


print('\n---------------COMPARED---------------')
compare(first_account, names[0], second_account, names[1], input_tweet)

print('\n~~~~~~~~~~~~~~~CREDITS~~~~~~~~~~~~~~~')
print("Helle van den Broek - Author")
print("Truls Andreas Berglund - Author")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
