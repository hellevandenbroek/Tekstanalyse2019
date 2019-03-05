import nltk
from nltk.corpus import brown

# A little bit unsure which grammar to use here
grammar = r"""
    NOUNP: {<DT>?<JJ.*>*<NN.*>+} # Noun phrase
    CLAUSE: {<VB><IN><NOUNP>}    # Verb
    """

cp = nltk.RegexpParser(grammar)
tagged = brown.tagged_sents()

def getClauses(cp, tagged):
    list_of_tuples = set()
    for sent in tagged:
        tree = cp.parse(sent)
        for subtree in tree.subtrees():
            if subtree.label() == 'CLAUSE':
                x = subtree[0][0]
                y = subtree[1][0]
                list_of_tuples.add((x,y, "NP"))
    return list_of_tuples

print('---------------EXERCISE1---------------')
result = (getClauses(cp, tagged))
x = 0
for i in result:
    if x < 20:
        print(i)
    x += 1

