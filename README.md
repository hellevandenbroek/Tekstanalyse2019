###### Note: Converted from PDF
# POETRY GENERATION BASED ON TWEETS
## GENERATING POEMS BASED ON TWEETS WITH THE USE OF THE NLTK LIBRARY FOR PYTHON
### WRITTENBY
#### HELLE VAN DEN BROEK & TRULS BERGLUND
#### NTNU
#### APRIL 2019
#### TDT 4310
## Abstract
This report documents the project work for the course Intelligent Tekst-
analyse og Språkforståelse (TDT4310) at the Norwegian University of Sci-
ence and Technology. The project is conducted by Helle van den Broek and
Truls Andreas Berglund, both studying for Bachelor in Informatics (BIT).
The goal for this project was to choose an assignment relevant to the
course, implement a solution and perform a presentation for the course pro-
fessors and other students at the end of the project.
The chosen project is the generating of poems, based on tweets from Twit-
ter accounts. Part of the goal was to use technologies and methods taught in
this course to return randomly generated poems based on different twitter
accounts. This was achieved using Tweepy for fetching tweets from the Twit-
ter API creating a corpus for a Twitter account and using the NLTK library
for python to create chunks of text which later can be put together resulting
in poems. This report documents the goals, implementation and results of
this project.
The end product is a program that can create corpora from different Twit-
ter accounts, removing unnecessary tokens and words, and saving it to a file.
The program then lets the user create poems, generated from chunks created
using the nltk.RegexParser on a certain grammar. It also lets the user select
whether they want a happy or sad poem using the python library TextBlob.
The poems may be saved to a poetry collection belonging to the relevant Twit-
ter account.
The end product meets the goals, and produces valid results, as well as
providing an intuitive user interface. The poems created are 4-lined po-
ems where the lines are all grammatically correct, written randomly and
are based on tweets from accounts on Twitter.
Even though generating poems by this approach proves for grammatically
correct lines resulting in proper looking quatrains, these results are unable
to deliver the meaning and depth often found in human written poetry. Pro-
gramming this might be more difficult, as computers lack the same emotions
and thoughts as human do (as of yet).
## Contents

    1 Introduction
        1.1 Motivation
        1.2 Goal
    2 Methods
        2.1 Chunking
        2.2 Sentiment Analysis
    3 Data
        3.1 Creating a corpus
        3.2 Example
    4 Implementation
        4.1 User Interface (UI)
        4.2 Corpus Creation
            4.2.1 Tweepy
            4.2.2 Fetching tweets
            4.2.3 Processing tweets
            4.2.4 Corpus creation
        4.3 Poetry Generation
            4.3.1 Fetching corpus
            4.3.2 Making chunks
            4.3.3 Using TextBlob to check semantics on chunks
            4.3.4 Putting chunks together
            4.3.5 Saving poems
    5 Results
        5.1 Donald Trump
        5.2 PETA
        5.3 Maisie Williams
        5.4 Elon Musk
        5.5 Adele
    6 Evaluation / Discussion
    7 Conclusion
    8 Sources
    9 Libraries

## 1 Introduction
1.1 Motivation

The motivation for this project was to generate poems using corpora with data
from Twitter accounts, while also implementing parts of the course syllabus into
the creation of the poetry. And so we had to ask ourselves: What is a poem? The
English Oxford Dictionaries defines a poem as following:

"A piece of writing in which the expression of feelings and ideas is given inten-
sity by particular attention to diction (sometimes involving rhyme), rhythm, and
imagery."

And where better to find someones feelings and expression than scraping their
twitter account?
1.2 Goal

The goal is to fetch tweets from different accounts and process them, such that
unnecessary words and tokens are removed, and the tweets are formatted in a
way they are usable as a corpus. After processing the corpus should be saved
to file, such that it can be fetched later for poetry generation. Ideally it should
be able to save the poems to files, such that we end up with collections of poems
from a chosen Twitter account. The sentences should be completely based on the
tweets from certain Twitter accounts, and it should be possible to generate both
sad and happy poems. Hopefully the poems will in some way be related to the
twitter accounts, and reflect some of the typical topics for the given account.
## 2 Methods

To reach this goal, two main methods have been used: chunking and sentiment
analysis.
2.1 Chunking

To create the lines in the poems, tweets needed to be taken apart to put them
back together again. To do this, chunking was used. Chunking is splitting the
text into several pieces and applying POS tagging on all the separate parts. The
modern language follow rules in order to create understandable sentences, for in-
stance, the sentence "I like pancakes" follows an order of [personal pronoun, verb,
noun(plural)]. When dealing with Natural Language Processing (NLP) there are
several types of grammars, one of them is Context-Free Grammar (CFG). This
one is straightforward as consist of sets of rules for combining components of
words into sensical sentences. NLTKs chunking method follows this procedure.
as can be seen in Figure 1, The strings are segmented and get assigned POS tags
at different levels. For this project a grammar was created, defining 4 different

Figure 1: Segmentation at chunk levels

types of chunks we wanted to find in the tweets. Later those 4 types of chunks can
be processed, mixed around, and in the end, put together to form grammatically
correct lines in a poem.
2.2 Sentiment Analysis

To create "happy" and "sad" poems, one needs to analyze lines of text and decide
whether they represent something negative or something positive. This is solved
using the machine learning based python library TextBlob. Tweets are separated
into chunks, and some of those chunks are checked for semantics to separate the
positive chunks from the negative ones. Sentiment Analysis is the process of
‘computationally’ determining whether a piece of writing is positive, negative
or neutral. Checking sentiments on only the smaller chunks of tweets, often
containing just a few words is much more accurate than it would be to analyze
entire tweets. The bigger the data set is, the more course the classification is,
and will result in a less accurate result.
## 3 Data
3.1 Creating a corpus

The data used in this project is fetched Twitter data from different Twitter ac-
counts. The tweets are fetched and processed to remove unnecessary tokens and
words. After the processing is done, the data gets saved to a .txt file. This is the
corpus, the data the poem generation is based on. The file name is always the
same as the username of the corresponding Twitter account. Each line in the file
represents one tweet.
3.2 Example

To give an example of what this might look like we can look at a excerpt from the
file elonmusk.txt, a corpus created based of the Twitter account @elonmusk:

C++ syntax sucks
Instagram comments are coding in emojis
Anyone who bought FSD will get it
Even connectivity at my house in Silicon Valley sucks!

## 4 Implementation
4.1 User Interface (UI)

In order to make the development and observation processes more fluent, an
easy-to-use UI was developed. This would benefit both the end user of the prod-
uct and the developers while working on and testing the program. All the func-
tionality for the UI is implemented in the app.py file. When the file is run it
provides the user with the following options: "add account" which creates new
corpora; "generate poem" which gives the possibility to generate poems; "show
stored accounts" which gives the user a list of stored corpora; "update corpus"
which will update an existing corpus with new tweets the Twitter user might
has tweeted since it was created and "exit application". The user also gets pre-
sented with additional options after choosing the ones mentioned, like choosing
whether they want happy or sad poem or deciding which account they want to
generate a corpus from.
4.2 Corpus Creation

Functionality for this can be found in the CreateCorpus class.
4.2.1 Tweepy

For fetching the desired tweets, Tweepy was used. Tweepy is an easy to use
Python library for accessing the twitter API, and returns back a Tweepy model
class instance containing various information.
4.2.2 Fetching tweets

Fetch the tweets from the Tweepy model class using:

api.user_timeline(screen_name=self.username,
tweet_mode=self.tweet_mode, count=self.count)

The count variable decides how many tweets we try to fetch from the API, and
can be easily changed by changing the variable value in the constructor. The
more data in our corpus, the better the poetry generator works.
4.2.3 Processing tweets

After all the tweets are fetched, we need to do some cleanup and process the found
tweets. Links and usernames are removed, as well as the “RT” that appears in
front of tweets that are retweets. Line breaks are also removed, and each tweet is
now one line only. There are a lot more things we could have chosen to do during
processing, for example removing retweets and emojis but we purposely chose to
leave them in, because the retweets gave us more data, and the emojis actually
turned out to lead to fun and interesting results.
4.2.4 Corpus creation

Like mentioned before, we want as much data in our corpus as possible, which
means we only want to accept Twitter accounts with more than a certain amount
of tweets on their timeline. If a user tries to add an account that does not have
sufficient data, they will be notified that it is not possible to add that account.
This variable is named minimum_tweets and is also defined in the constructor
and easy to change if one would like to increase or decrease this amount of abso-
lute minimum tweets the account must contain. After the tweets are processed
the corpus is saved to a .txt file, as long as there are a sufficient amount of tweets
in the corpus. The .txt file contains one tweet for each line.
4.3 Poetry Generation

Code for this implementation can be found in the class BasePoetryGenerator.
4.3.1 Fetching corpus

The corpus is fetched from an existing .txt file containing tweets, and is saved to
a variable declared in the instructor.
4.3.2 Making chunks

The general generation of poetry is based on creating chunks of grammar based
on the tweets from the corpus. There are many different ways to do this, but
we decided to create a grammar ourselves, that would return different chunks of
tweets, that we could later put together to make somehow meaningful, grammat-
ical correct sentences to form poems.

grammar = r"""
NP: {
}
NOUNP: {
?<JJ.><NN*>+}
CLAUSE: {}
WRB: {}
"""
cp = nltk.RegexParser(grammar)
result = cp.parse(sent)

Using the nltk.RegexParser on the grammar and later parsing every sentence
in the corpus to find chunks that satisfy the grammar defined, we end up with
a list of all the different chunks above. It is absolutely possible to play around
with the grammar, and changing it up as one likes. It is possible to make the
chunks less strict (e.g. making some of the parts in the chunks optional), or
making it more strict (e.g. making parts required). There are endless possibilities
and combinations of grammar, one could make the chunks longer, shorter or just
create totally new chunks.
4.3.3 Using TextBlob to check semantics on chunks

This poetry generator also lets the user choose whether they want negative or
positive poems. To implement this, the semantics of chunks are checked using
TextBlob, and based on the polarity score it gets determined to be either positive,
negative or neutral.

sentiment = TextBlob(sent).sentiment.polarity

4.3.4 Putting chunks together

After the semantics are added, chunks are put together to form poems.

first_line = self.np[random.randint(0, lenNP)]
second_line = self.clause[random.randint(0, lenClause)]
third_line = self.wrb[random.randint(0, lenWrb)]
+ self.np[random.randint(0, lenNP)]
fourth_line = self.np[random.randint(0, lenNP)]

Each line in the poem consists of chunks randomly selected from a list of a
certain type of chunks, e.g the first line, which consists of a random "np" chunk.
Right now we put four lines together from different chunks, but this is easily
changeable if one would like to experiment with different combinations.
4.3.5 Saving poems

Finally the user gets the option to save tweets if they like what is generated. In
that case, another .txt file gets created and the saved tweets are appended to this
file.
## 5 Results

Each poem presented here consists of four lines. This is also known as a quatrain.
The results have been categorized into happy and sad poems, as was part of the
poetry generation task.
5.1 Donald Trump

Twitter account:realDonaldTrump
Negative poems:

the phony collusion
as last hope
than no underlying crime
a bad thing

Positive poems:

a major win
in the best shape
on a great job
the GREAT STATE

the first time
additional large scale
in The good news
the first time

5.2 PETA

Twitter account:peta
Negative poems:

the animal overpopulation
on day
for the misguided belief
a diverse group

an urgent matter
into small dirt
at a reputable sanctuary
the animal overpopulation

Positive poems:

the new movie
for the love
for a great way
a reputable sanctuary

a wild animal
with the right
of an amazing decision
the good news

5.3 Maisie Williams

Twitter account:maisie_williams
Negative poems

a virtual world
like i
at the final season
a career-focused platform

the final piece
nuuuuumber oooooone ’
while a little ’
a performant app

Positive poems:

a major spoiler
in good time
If a wonderful afternoon
a major spoiler

a fast track
of creative collaboration
of a fast track
the first run...

5.4 Elon Musk

Twitter account:elonmusk
Negative poems:

a particulate filter
of the cosmos
for a big deal
a winsome eyre

Positive poems:

a real question
for full refund
for an absolute unit
a good reason

5.5 Adele

Twitter account:adele
Negative poems:

A short blog
on the grind
with the other side
a Chinese watching

Positive poems:

a wonderful beyday
without clean drinking water
in a wonderful time
a wonderful night

## 6 Evaluation / Discussion

Several types of accounts were used to get results. These types include actors,
artists, politicians and organizations. This was done in order to get a wide scope
of content, resulting in a range of different topics and a visible variation in the
topics of the lines in the quatrains related to the different accounts.
On some of the poems we generated, the sentimentality is often subtle. The
first gloomy poem generated by Maisie Williams does not seem like a sad poem.
The words for these lines were chosen, using the aforementioned TextBlob li-
brary, and returned as the composition of words from the corpus with the correct
sentimental value (positive or negative). There are several possible reasons for
this: Maisie Williams might be posting positive tweets rather than depressing
and tragic tweets, making it less probable to find tweets with negative connota-
tions. Another reason might be her tweets containing a certain high amount of
sarcasm, which makes it harder for the library to determine the sentimentality.

An example where the positive tweets are more distinct from the negative, is
with Donald Trump. The first positive tweet includes key words such as "win",
"best", "great", among other words. The negative poem contains key words such
as "phony", "last", "crime" and the obvious "bad". These poems may help de-
termine an account’s idiolect when it comes to positivity and negativity. Don-
ald Trump seems to write tweets using easy-to-understand phrases such as "bad
thing", instead of writing something like "terrible occurrence". Donald Trumps
phrasing might provide a more abstract image, and might therefore be better
suited for poetry.

The use of chunks to segment the different tweets, and assigning POS tagging at
different levels, makes the individual lines of the poems grammatically correct.
The poems as a whole, on the other hand, are not guaranteed to be grammati-
cally correct. The first line in Donald Trumps negative poem reads "the phony
collusion", which is a grammatically correct part of a sentence. One understands
that the topic is of a specific collusion that is phony.
However, reading the rest of the poem, the grammar as a whole seem to have
some holes. The composition "as last hope" makes grammatically sense on its
own, but combined with the line above, it seems to be missing an "a". "The phony
collusion as a last hope" reads easier and do not have the same error as in the
poem. Expanded work could have been made to tune the poems with a bigger
grammatically correct scope, but was chosen to be out of scope for this particular
project.

Given more time and resources, other features from poetry would be implemented.
These are features such as rhyme, alliteration, assonance and so on. Making
rhymes with the generator would be to look for chunks with end words that corre-
late with end words in other chunks, for instance "if only my sorrow" and "would
be gone tomorrow". The most popular one, from a programming perspective,
would be the words ending with "-ing", as these would be the easiest to use when

combining lines in poems.
Adele’s positive tweet consists of several w’s on each line, and seems to make
use of alliteration. This is random chance, but a program could be created to
favour certain characters when deciding the phrases to use as well as imple-
menting the features mentioned above. This will not be done in this project, but
is an interesting discussion for potential future works, as the opportunities are
nearly endless since the "structure" of poetry is very fluent and exist in countless
forms.
## 7 Conclusion

It is fair to conclude that this project has been a success in the sense that the
project goals have been met. The outcome of the tweets fetching combined with
the generating of tweets has resulted in collections of tweets that in some cases
could resemble the writing of a human. Even though not all the poems make
sense, one could argue that poems not always do, as they are abstract pieces of
writing, often having more meaning than just their literal interpretation. Rel-
evant topics for different Twitter accounts are often mentioned in the poems,
which makes it possible to relate many poems to the accounts they are based
from.

So even though these poems, based on randomly put together lines, might lack
the purpose and deeper meaning a human-written poem might contain, they def-
initely resemble poems written by humans in the past. And even though the
computer generated lines are put together randomly, without taking context to
each other into account, in many cases they actually make sense.
## 8 Sources

    http://www.tweepy.org/
    https://textblob.readthedocs.io/en/dev/
    https://en.oxforddictionaries.com/definition/poem
    https://www.nltk.org/book/ch07.html, Figure 1

## 9 Libraries

    Tweepy, http://www.tweepy.org/
    NLTK, http://www.nltk.org/
    TextBlob, https://textblob.readthedocs.io/en/dev/

