#TODO: make corpus great again. Get 200 tweets from input user
#TODO: treat corpus
#TODO: Ngrams, få dette til å bli riktig
#TODO: poetry generation

from twitterCorpus import CorpusGenerator


user = input("Type in a twitter-account you want to generate poetry from: ")
cp = CorpusGenerator(user)
cp.save_to_file()
