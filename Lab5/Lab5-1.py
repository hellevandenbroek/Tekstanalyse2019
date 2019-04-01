import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import tree2conlltags

#Sources: https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da

def readFromFile():
    f = open("SpaceX.txt", "r", encoding="utf-8")
    lines = ""
    for line in f.readlines():
        lines += line
    return lines


def preprocess(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


doc = readFromFile()
sent = preprocess(doc)
grammar = 'NP: {<DT>?<JJ>*<NN>}'
cp = nltk.RegexpParser(grammar)
cs = cp.parse(sent)
iob_tagged = tree2conlltags(cs)
ne_tree = nltk.ne_chunk(pos_tag(word_tokenize(doc)))


def unique(tree):
    unique_tree = []
    for t in tree:
        if t not in unique_tree:
            unique_tree.append(t)
    return unique_tree


print("\n---------------ENTITY NAMES---------------")
print(ne_tree)


print("\n---------------UNIQUE ENTITY NAMES---------------")
unique_list = (unique(ne_tree))
for i in unique_list:
    print(i)

print("\n---------------LEXICAL ASCENDING ENTITY NAMES---------------")
unique_list.sort()
for i in unique_list:
    print(i)
