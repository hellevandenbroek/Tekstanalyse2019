#!/usr/bin/env python3
import nltk


grammar = "NP: {<NNP>*|<DT>?<JJ>?<NNS>|<NN><NN>}"
p = nltk.RegexpParser(grammar)

with open("SpaceX.txt") as f:
    first5Lines=f.readlines()[0:5]

tagged_sents = []
for line in first5Lines:
  tagged_sent = nltk.pos_tag(nltk.word_tokenize(line))
  tagged_sents.append(tagged_sent)

parsed_sents = []
for tagged_sent in tagged_sents:
  parsed_sent = p.parse(tagged_sent)
  parsed_sents.append(parsed_sent)

matches = []
for parsed_sent in parsed_sents:
  for subtree in parsed_sent.subtrees():
    if subtree.label() == 'NP':
      matches.append(subtree[0][0])

for match in set(matches):
  if match != "]": # A bug where ] is seen as a match for NP
    print(match)

