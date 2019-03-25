#TODO: make corpus great again. Get 200 tweets from input user
#TODO: treat corpus
#TODO: Ngrams, få dette til å bli riktig
#TODO: poetry generation

import makeCorpus
import handleCorpus

user = input("Type in a twitter-account you want to generate poetry from: ")
makeCorpus.make_corpus(user)

