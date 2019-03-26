import nltk

import random
import pathlib


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
        self.np = []
        self.clause = []
        self.wrb = []
        self.poem = ""

        pathlib.Path('Poems').mkdir(exist_ok=True)


    def fetch_tweets(self):
        print('Now generating a poem based on the tweets from {}......'.format(self.username))
        corpus = []
        file = open("./Corpus/{}.txt".format(self.username),"r", encoding="utf-8")
        for line in file:
            corpus.append(line)
        self.corpus = corpus
        self.make_chunks()


    def make_chunks(self):
        document = self.corpus
        grammar = r"""
            NP: {<DT><JJ><NN>} # Noun phrase
            NOUNP: {<DT>?<JJ.*>*<NN*>+} # Noun phrase used for clauses
            CLAUSE: {<IN><NOUNP>}    # Verb
            WRB: {<IN>}
        """
        cp = nltk.RegexpParser(grammar)
        nps = []
        clauses = []
        wrbs = []

        for sentence in document:
            sent = nltk.word_tokenize(sentence)
            sent = nltk.pos_tag(sent)
            result = cp.parse(sent)

            #We now find noun phrases and clauses to use in our poems
            for subtree in result.subtrees():
                if subtree.label() == 'NP':
                    line = ""
                    for word in subtree.leaves():
                        line += word[0]
                        line += " "
                    nps.append(line)

                elif subtree.label() == 'CLAUSE':
                    line = ""
                    for word in subtree.leaves():
                        line += word[0]
                        line += " "
                    clauses.append(line)

                elif subtree.label() == 'WRB':
                    line = ""
                    for word in subtree.leaves():
                        line += word[0]
                        line += " "
                    wrbs.append(line)

        self.np = nps
        self.clause = clauses
        self.wrb = wrbs

    def print_poem(self):
        print(" ")
        print("Based of: ")
        print(self.username)
        print(" ")
        lenNP = len(self.np)
        lenClause = len(self.clause)
        lenWrb = len(self.wrb)

        first_line = self.np[random.randint(0, lenNP)]
        second_line = self.clause[random.randint(0, lenClause)]
        third_line = self.wrb[random.randint(0, lenWrb)] + self.np[random.randint(0, lenNP)]
        fourth_line = self.np[random.randint(0, lenNP)]

        self.poem = "{}\n{}\n{}\n{}".format(first_line, second_line, third_line, fourth_line)
        print(self.poem)
        print(" ")

    def save_poem(self):
        # Save to file
        if self.poem == "":
            return
        try:
            file = open("Poems/{}.txt".format(self.username.lower()), "ab")
            file.write(self.poem.encode() + '\n'.encode())
        finally:
            file.close()
            print("Added poem to collection of {} ".format(self.username))


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


