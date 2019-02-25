import nltk
from nltk.corpus import brown
from nltk.corpus import nps_chat


def splitting(list) :

    middle = int(len(list)/2)
    splitpoint = int((len(list)/100)*90)

    train_1 = list[0:middle]
    test_1 = list[middle:len(list)]
    train_2 = list[0:splitpoint]
    test_2 = list[splitpoint:len(list)]

    return train_1, train_2, test_1, test_2


def ex2() :

    tagged_brown = brown.tagged_sents(categories = 'news')

    results_brown = splitting(tagged_brown)
    train_brown1 = results_brown[0]
    train_brown2 = results_brown[1]
    test_brown1 = results_brown[2]
    test_brown2 = results_brown[3]

    tagged_chat = nps_chat.tagged_posts()
    results_chat = splitting(tagged_chat)
    train_chat1 = results_chat[0]
    train_chat2 = results_chat[1]
    test_chat1 = results_chat[2]
    test_chat2 = results_chat[3]

    default_tagger = nltk.DefaultTagger('NN')
    default_tagger.tag(test_brown1)
    default_tagger.tag(test_brown2)
    default_tagger.tag(test_chat1)
    default_tagger.tag(test_chat2)

    print('Test for brown corpus 1 : {}'.format(default_tagger.evaluate(test_brown1)))
    print('Test for brown corpus 2 : {}'.format(default_tagger.evaluate(test_brown2)))
    print('Test for chat corpus 1 : {}'.format(default_tagger.evaluate(test_chat1)))
    print('Test for chat corpus 2 : {}'.format(default_tagger.evaluate(test_chat2)))

    t1 = nltk.UnigramTagger(train_brown1, backoff=default_tagger)
    print(t1.evaluate(test_brown1))
    t2 = nltk.BigramTagger(train_brown1, backoff=t1)
    print(t2.evaluate(test_brown1))
    t3 = nltk.TrigramTagger(train_brown1, backoff=t2)
    print('Accuracy test brown 1: ', t3.evaluate(test_brown1))

    t1 = nltk.UnigramTagger(train_brown2, backoff=default_tagger)
    print(t1.evaluate(test_brown2))
    t2 = nltk.BigramTagger(train_brown2, backoff=t1)
    print(t2.evaluate(test_brown2))
    t3 = nltk.TrigramTagger(train_brown2, backoff=t2)
    print('Accuracy test brown 2: ', t3.evaluate(test_brown2))

    t1 = nltk.UnigramTagger(train_chat1, backoff=default_tagger)
    print(t1.evaluate(test_chat1))
    t2 = nltk.BigramTagger(train_chat1, backoff=t1)
    print(t2.evaluate(test_chat1))
    t3 = nltk.TrigramTagger(train_chat1, backoff=t2)
    print('Accuracy test chat 1: ', t3.evaluate(test_chat1))

    t1 = nltk.UnigramTagger(train_chat2, backoff=default_tagger)
    print(t1.evaluate(test_chat2))
    t2 = nltk.BigramTagger(train_chat2, backoff=t1)
    print(t2.evaluate(test_chat2))
    t3 = nltk.TrigramTagger(train_chat2, backoff=t2)
    print('Accuracy test chat 2: ', t3.evaluate(test_chat2))


ex2()


