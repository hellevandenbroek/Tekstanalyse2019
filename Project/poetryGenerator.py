import nltk
from nltk.corpus import brown

class PoetryGenerator:
    """
        This class contains the creation of the
        poems. This makes use of the files from
        the Corpus directory.
    """
    def __init__(self, username):
        self.foo = "bar"
        self.username = username
        self.corpus = []
        self.fetch_tweets()

    def fetch_tweets(self):
        print(self.username)
        corpus = []
        file = open("./Corpus/{}.txt".format(self.username),"r", encoding="utf-8")
        for line in file:
            corpus.append(line)
        self.corpus = corpus

        self.make_chunks()


    def make_chunks(self):

        document = self.corpus

        grammar = "NP: {<DT>?<JJ>*<NN>}"

        cp = nltk.RegexpParser(grammar)

        for sentence in document:
            sent = nltk.word_tokenize(sentence)
            sent = nltk.pos_tag(sent)
            result = cp.parse(sent)
            print(result)


    def getClauses(self, cp, tagged):
        list_of_tuples = set()
        for sent in tagged:
            tree = cp.parse(sent)
            for subtree in tree.subtrees():
                if subtree.label() == 'CLAUSE':
                    x = subtree[0][0]
                    y = subtree[1][0]
                    list_of_tuples.add((x,y, "NP"))
        return list_of_tuples



# comment about what each part of speech is:
""" CC   - conjunction: or, but, and, either
    CD   - number: one, two, three
    DT   - determiner: a, an, the, both, all, these, any, some
    EX   - the word 'there'
    IN   - preposition: in, of, with, for, under, among, upon, at
    JJ   - adjective: certain, curious, little, golden, other, offended
    JJS  - adjective: -est : best, loveliest, largest
    JJR  - adjective: -er : lerger, smaller, worse
    MD   - can, dare, should, will*, might, could, must
    NN   - common singular noun
    NNS  - common plural noun
    NNP  - proper singular noun
    NNPS - proper plural noun
    PDT  - all, both, quite, many, half
    PRP  - hers, her, himself, thy, us, it, I, him, you, they
    PRPP - possesive: his, mine, our, my, her, its, your
    RB   - adverb: very, not, here, there, first, just, down, again, beautifully, -ly
    RBR  - more
    RBS  - adverb superlative: -est
    RP   - participle: up, down, out, away, over, off
    TO   - the word 'to'
    UH   - interjection
    VB   - vocative verb: to ___ 
    VBD  - past verb: -ed : was*(freq. occur), had, dipped, were, said, seemed
    VBG  - present verb: -ing: trembling, trying, getting, running, swimming
    VBN  - past verb descriptive: crowded, mutated, fallen, lit, lost, forgtten
    VBP  - present verb: not -s: am, wish, make, know, do, find
    VBZ  - present verb: -s : is*, has, seems
    WDT  - what, which, that*
    WP   - who, what
    WRB  - how, whenever, where, why, when
"""


