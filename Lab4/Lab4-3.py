import nltk
from nltk import word_tokenize


def process(document):
   sentences = nltk.sent_tokenize(document)
   sentences = [nltk.word_tokenize(sent) for sent in sentences]
   sentences = [nltk.pos_tag(sent) for sent in sentences]
   return sentences


def readFromFile():
    f = open("SpaceX.txt", "r", encoding="utf-8")
    lines = ""
    limit = 5
    for line in f.readlines():
        if limit > 0:
            lines += line
        limit -= 1
    return lines

grammar = r"""
    NP: {<NNP>*}
        {<DT>?<JJ>?<NNS>}
        {<NN><NN>}"""

document = readFromFile()
processed_doc = process(readFromFile())
cp = nltk.RegexpParser(grammar)
result = cp.parse(processed_doc[0])

print('\n---------------THE DOCUMENT---------------')
print(document)

print('\n---------------THE PROCESSED DOCUMENT---------------')
print(processed_doc)

print('\n---------------PARSED---------------')
print(result)

print('\n---------------MATCHES---------------')
matches = []
for sent in processed_doc:
    tree = cp.parse(sent)
    for subtree in tree.subtrees():
        if subtree.label() == 'NP':
            matches.append(subtree[0][0])
print(matches)

print(result.draw())

