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


def ex3() :

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


    fd = nltk.FreqDist(brown.words(categories='news'))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))

    most_freq_words = fd.most_common(200)
    likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
    baseline_tagger = nltk.UnigramTagger(model=likely_tags)

    tb1_t1 = nltk.UnigramTagger(test_brown1, backoff=baseline_tagger)
    tb1_t2 = nltk.BigramTagger(train_brown1, backoff=tb1_t1)
    tb1_t3 = nltk.TrigramTagger(train_brown1, backoff=tb1_t2)
    
    tb2_t1 = nltk.UnigramTagger(test_brown2, backoff=baseline_tagger)
    tb2_t2 = nltk.BigramTagger(train_brown2, backoff=tb2_t1)
    tb2_t3 = nltk.TrigramTagger(train_brown2, backoff=tb2_t2)

    # test_brown 1
    print("test brown 1")
    print(tb1_t1.evaluate(test_brown1))
    print(tb1_t2.evaluate(test_brown1))
    print(tb1_t3.evaluate(test_brown1))
    
    # test_brown 2
    print("test brown 2")
    print(tb2_t1.evaluate(test_brown2))
    print(tb2_t2.evaluate(test_brown2))
    print(tb2_t3.evaluate(test_brown2))


    tc1_t1 = nltk.UnigramTagger(test_chat1, backoff=baseline_tagger)
    tc1_t2 = nltk.UnigramTagger(test_chat1, backoff=tc1_t1)
    tc1_t3 = nltk.UnigramTagger(test_chat1, backoff=tc1_t2)

    tc2_t1 = nltk.UnigramTagger(test_chat2, backoff=baseline_tagger)
    tc2_t2 = nltk.UnigramTagger(test_chat2, backoff=tc2_t1)
    tc2_t3 = nltk.UnigramTagger(test_chat2, backoff=tc2_t2)

    print("test chat 1")
    print(tc1_t1.evaluate(test_chat1))
    print(tc1_t2.evaluate(test_chat1))
    print(tc1_t3.evaluate(test_chat1))

    print("test chat 2")
    print(tc2_t1.evaluate(test_chat2))
    print(tc2_t2.evaluate(test_chat2))
    print(tc2_t3.evaluate(test_chat2))

ex3()


