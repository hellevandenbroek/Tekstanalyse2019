#!/usr/bin/env python3
from nltk import word_tokenize

"""
    Code fetched from:
    https://github.com/foxbook/atap/blob/master/snippets/ch07/model.py
"""

import nltk

from math import log
from collections import Counter, defaultdict

from nltk.util import ngrams

from nltk.probability import ProbDistI, FreqDist, ConditionalFreqDist


def count_ngrams(n, vocabulary, texts):
    counter = NgramCounter(n, vocabulary)
    counter.train_counts(texts)
    return counter


class NgramCounter(object):
    """
    The NgramCounter class counts ngrams given a vocabulary and ngram size.
    """

    def __init__(self, n, vocabulary, unknown="<UNK>"):
        """
        n is the size of the ngram
        """
        if n < 1:
            raise ValueError("ngram size must be greater than or equal to 1")

        self.n = n
        self.unknown = unknown
        self.padding = {
            "pad_left": True,
            "pad_right": True,
            "left_pad_symbol": "<s>",
            "right_pad_symbol": "</s>"
        }

        self.vocabulary = vocabulary
        self.allgrams = defaultdict(ConditionalFreqDist)
        self.ngrams = FreqDist()
        self.unigrams = FreqDist()

    def train_counts(self, training_text):
        for sent in training_text:
            checked_sent = (self.check_against_vocab(word) for word in sent)
            sent_start = True
            for ngram in self.to_ngrams(checked_sent):
                self.ngrams[ngram] += 1
                context, word = tuple(ngram[:-1]), ngram[-1]
                if sent_start:
                    for context_word in context:
                        self.unigrams[context_word] += 1
                    sent_start = False

                for window, ngram_order in enumerate(range(self.n, 1, -1)):
                    context = context[window:]
                    self.allgrams[ngram_order][context][word] += 1
                self.unigrams[word] += 1

    def check_against_vocab(self, word):
        if word in self.vocabulary:
            return word
        return self.unknown

    def to_ngrams(self, sequence):
        """
        Wrapper for NLTK ngrams method
        """
        return ngrams(sequence, self.n, **self.padding)


class BaseNgramModel(object):
    """
    The BaseNgramModel creates an n-gram language model.
    This base model is equivalent to a Maximum Likelihood Estimation.
    """

    def __init__(self, ngram_counter):
        """
        BaseNgramModel is initialized with an NgramCounter.
        """
        self.n = ngram_counter.n
        self.ngram_counter = ngram_counter
        self.ngrams = ngram_counter.ngrams
        self._check_against_vocab = self.ngram_counter.check_against_vocab

    def check_context(self, context):
        """
        Ensures that the context is not longer than or equal to the model's
        n-gram order.
        Returns the context as a tuple.
        """
        if len(context) >= self.n:
            raise ValueError("Context too long for this n-gram")

        return tuple(context)

    def score(self, word, context):
        """
        For a given string representation of a word, and a string word context,
        returns the maximum likelihood score that the word will follow the
        context.
        """
        context = self.check_context(context)

        return self.ngrams[context].freq(word)

    def logscore(self, word, context):
        """
        For a given string representation of a word, and a word context,
        computes the log probability of this word in this context.
        """
        score = self.score(word, context)
        if score == 0.0:
            return float("-inf")

        return log(score, 2)

    def entropy(self, text):
        """
        Calculate the approximate cross-entropy of the n-gram model for a
        given text represented as a list of comma-separated strings.
        This is the average log probability of each word in the text.
        """
        normed_text = (self._check_against_vocab(word) for word in text)
        entropy = 0.0
        processed_ngrams = 0
        for ngram in self.ngram_counter.to_ngrams(normed_text):
            context, word = tuple(ngram[:-1]), ngram[-1]
            entropy += self.logscore(word, context)
            processed_ngrams += 1
        return - (entropy / processed_ngrams)

    def perplexity(self, text):
        """
        Given list of comma-separated strings, calculates the perplexity
        of the text.
        """
        return pow(2.0, self.entropy(text))


class KneserNeyModel(BaseNgramModel):
    """
    Implements Kneser-Ney smoothing
    """
    def __init__(self, *args):
        super(KneserNeyModel, self).__init__(*args)
        self.model = nltk.KneserNeyProbDist(self.ngrams)

    def score(self, word, context):
        """
        Use KneserNeyProbDist from NLTK to get score
        """
        trigram = tuple((context[0], context[1], word))
        return self.model.prob(trigram)

    def samples(self):
        return self.model.samples()

    def prob(self, sample):
        return self.model.prob(sample)


def readFromFile():
    # trying without SW
    f = open("twitterCorpus.txt", "r", encoding="utf-8")
    tweets = []
    names = []
    for line in f.readlines():
        tweeter = line
        colon = tweeter.index(":")
        name = tweeter[0:colon]
        names.append(name)
        only_tweets = tweeter[colon + 1:]
        new_tweeter = only_tweets.split('-,-')
        for tw in new_tweeter:
            tweets.append(tw.lower())
    return tweets, names


def tokenize(tweets):
    tokens = []
    for tweet in tweets:
        tokens += [word_tokenize(tweet)]
    return tokens


if __name__ == '__main__':
    corpus_from_file = readFromFile()
    tweets = corpus_from_file[0]

    print('Tweets: ', tweets)

    tokens = tokenize([''.join(tweet) for tweet in tweets])

    full = []
    for item in tokens:
        for boom in item:
            full.append(boom)

    vocab = Counter(full)
    counter = count_ngrams(3, vocab, tokens)
    knm = KneserNeyModel(counter)

    def complete(input_text):
        highest_value = 0
        tokenized = nltk.word_tokenize(input_text)
        if len(tokenized) < 2:
            response = "Say more."
        else:
            completions = {}
            prob_value = []
            for sample in knm.samples():
                if (sample[0], sample[1]) == (tokenized[-2], tokenized[-1]):
                    completions[sample[2]] = knm.prob(sample)
                    prob_value.append(knm.prob(sample))
            if len(completions) == 0:
                response = "Can we talk about something else?"
            else:
                best = max(
                    completions.keys(), key=(lambda key: completions[key])
                )
                highest_value = max(prob_value)
                tokenized += [best]
                response = " ".join(tokenized)
        return response, highest_value

    def format_complete(input_text):
        com = complete(input_text)
        if com == "Can we talk about something else?":
            return "Unable to find an answer to this."
        return "The calculated completed word for the input: '{}' was:\n {}\n Probability: {}\n~~~~~~".format(input_text, com[0], com[1])

    print(format_complete("hiv is"))
    print(format_complete("crooked hillary"))
    print(format_complete("make america great"))
