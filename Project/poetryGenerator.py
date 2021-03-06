import nltk
import random
import pathlib
from textblob import TextBlob

class BasePoetryGenerator:
    """
    Simple Base class for Poetry Generator. Might be useful
    if different PoetryGenerators are made and all require basic
    functions.
    """

    def __init__(self, username):
        self.foo = "bar"
        self.username = username
        self.corpus = []
        self.np = []
        self.clause = []
        self.wrb = []
        self.poem = ""

    def print_poem(self):
        print("\n Based of: \n", self.username, "\n")
        print(self.poem, "\n")

    def save_poem(self):
        if self.poem == "":
            return
        try:
            file = open("Poems/{}.txt".format(self.username.lower()), "ab")
            file.write(self.poem.encode() + '\n\n'.encode())
        finally:
            file.close()
            print("Added poem to collection of {} ".format(self.username))

    def fetch_tweets(self):
        print('Now generating a poem based on the tweets from {}......'.format(self.username))
        corpus = []
        file = open("./Corpus/{}.txt".format(self.username),"r", encoding="utf-8")
        for line in file:
            corpus.append(line)
        self.corpus = corpus


class PoetryGenerator(BasePoetryGenerator):
    """
        This class contains the creation of the
        poems. This makes use of the files from
        the Corpus directory. Builds on BasePoetryGenerator
    """

    def __init__(self, username, mood):
        super(PoetryGenerator, self).__init__(username)
        self.corpus = []
        self.np = []
        self.clause = []
        self.wrb = []
        self.mood = self.determine_input_mood(mood)
        self.poem = ""

        pathlib.Path('Poems').mkdir(exist_ok=True)

    def determine_input_mood(self, word):
        if word.startswith("h" or 'H'):
            return "happy"
        return "sad"


    def make_chunks(self):
        document = self.corpus
        grammar = r"""
            NP: {<DT><JJ><NN>} # Noun phrase
            NOUNP: {<DT>?<JJ.*>*<NN*>+} # Noun phrase used for clauses
            CLAUSE: {<IN><NOUNP>}    # Verb
            WRB: {<IN>}
        """
        cp = nltk.RegexpParser(grammar)
        nps_happy = []
        clauses_happy = []
        wrbs = []
        nps_sad = []
        clauses_sad = []

        for sentence in document:
            sent = nltk.word_tokenize(sentence)
            sent = nltk.pos_tag(sent)
            result = cp.parse(sent)
            # We now find noun phrases and clauses to use in our poems
            for subtree in result.subtrees():
                if subtree.label() == 'NP':
                    line = ""
                    for word in subtree.leaves():
                        line += word[0]
                        line += " "
                    if self.check_semantic(line):
                        nps_happy.append(line)
                    else:
                        nps_sad.append(line)
                elif subtree.label() == 'CLAUSE':
                    line = ""
                    for word in subtree.leaves():
                        line += word[0]
                        line += " "
                    if self.check_semantic(line):
                        clauses_happy.append(line)
                    else:
                        clauses_sad.append(line)
                elif subtree.label() == 'WRB':
                    line = ""
                    for word in subtree.leaves():
                        line += word[0]
                        line += " "
                    wrbs.append(line)
        if self.mood == 'happy':
            self.np = nps_happy
            self.clause = clauses_happy
        if self.mood == 'sad':
            self.np = nps_sad
            self.clause = clauses_sad
        self.wrb = wrbs

    def check_semantic(self, sent):
        sentiment = TextBlob(sent).sentiment.polarity
        if sentiment > 0:
            return True
        elif sentiment < 0:
            return False
        #Option for neutral
        else:
            return False

    def create_poem(self):
        lenNP = len(self.np)-1
        lenClause = len(self.clause)-1
        lenWrb = len(self.wrb)-1

        first_line = self.np[random.randint(0, lenNP)]
        second_line = self.clause[random.randint(0, lenClause)]
        third_line = self.wrb[random.randint(0, lenWrb)] + self.np[random.randint(0, lenNP)]
        fourth_line = self.np[random.randint(0, lenNP)]
        self.poem = "{}\n{}\n{}\n{}".format(first_line, second_line, third_line, fourth_line)
        self.print_poem()

    def main(self):
        self.fetch_tweets()
        self.make_chunks()
        self.create_poem()

        print("Want to save this poem to disk? y/n")
        save = input(">")
        if save.startswith("y"):
            self.save_poem()

# Part of speech cheat note:
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


