import random
import nltk
from nltk.corpus import movie_reviews, wordnet
from nltk.classify import apply_features


#Does not work :'(
def synsets(words):
    syns = set()
    for word in words:
        syns.update(str(s) for s in wordnet.synsets(word))

    return syns


# retrieve all movie reviews in the form of (wordlist, category)
# randomize the documents so any default category ordering is removed
documents = [(list(movie_reviews.words(fileid)), category) for category in movie_reviews.categories() for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]
synset_features = synsets(word_features)


def document_features(document):
    document_words = set(document)
    document_synsets = synsets(document_words)
    features = {}
    features2 = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)

    for synset in synset_features:
        features2[synset] = (synset in document_synsets)

    return features, features2

featuresets = [(document_features(d)[0], c) for (d,c) in documents]
train_set, test_set = featuresets[100:], featuresets[:100]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print('\n---------------ORIGINAL---------------')
print('Accuracy = {}'.format(nltk.classify.accuracy(classifier, test_set)))
classifier.show_most_informative_features(5)



featuresets2 = [(document_features(d)[1], c) for (d,c) in documents]
train_set2, test_set2 = featuresets2[100:], featuresets2[:100]
classifier2 = nltk.NaiveBayesClassifier.train(train_set2)

print('\n---------------SYNSET-BASED---------------')
print('Accuracy = {}'.format(nltk.classify.accuracy(classifier, test_set2)))
classifier2.show_most_informative_features(5)