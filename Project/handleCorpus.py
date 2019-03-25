#TODO: remove links and "RT" and stuff like that
from twitterCorpus import CorpusGenerator

cp = CorpusGenerator("realDonaldTrump")
print(cp.tweets[0])
cp.save_to_file()