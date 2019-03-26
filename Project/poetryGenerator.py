import nltk


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
        print(self.corpus)

    def make_chunks(self):

        document = self.corpus

        sentences = nltk.sent_tokenize(document)
        sentences = [nltk.word_tokenize(sent) for sent in sentences]
        sentences = [nltk.pos_tag(sent) for sent in sentences]

        grammar = "NP: {<DT>?<JJ>*<NN>}"

        cp = nltk.RegexpParser(grammar)

        for sentence in sentences:
            result = cp.parse(sentence)
            print(result)


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


