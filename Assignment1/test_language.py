import nltk

from nltk.corpus import gutenberg as gb
from nltk.corpus import brown


# https://pandas.pydata.org/
# https://keras.io/
# https://scikit-learn.org/stable/


TEXT = "TODAY I SAW THE SANTA CLAUS BUT IT IS NOT CHRISTMAS"

tokens = nltk.word_tokenize(TEXT)

# List all documents in the corpora
print(gb.fileids())

# count number of characters
print(len(gb.raw('austen-emma.txt')))


# count number of words
print(len(gb.words('austen-emma.txt')))

# number of sentences
print(gb.sents('austen-emma.txt'))

# words between 11 and 40
print(''.join(gb.words('austen-emma.txt')[11:40]))


# brown corpus

# cfd = nltk.ConditionalFreqDist((genre, word)
# for genre in brown.categories():
#     for word in brown.words(categories=genre):
#         print(word)
#         )
# genres = ['news', 'entertainment']




    

