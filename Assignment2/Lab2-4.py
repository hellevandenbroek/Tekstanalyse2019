# HMM in Python

# The HMM is usually used in the problem of POS tagging.
# Probability of a tag sequence for a sequence is illutrated as follows:
# Original Resource: from internet :d
# for a given words = w1....wN with tags = t1..tN
#
# then
# P(tags | words) = \PI P(ti | t{i-1}) P(wi | ti)
#
# The best tag sequence for a given sequence of words is a tag thatwe has the maximum P(tags | words)

import nltk
import sys
from nltk.corpus import brown

# We utilize Maximum Likelihood Estimation (MLE):
# P(wi | ti) = count(wi, ti) / count(ti)
# to estimate P(wi | ti) from corpus data 
# brown is our corpus in this exercise
"""
    function: corpus_tags
        Args:
            corpus

        Returns: get all tags of the corpus 
"""
def get_tags(corpus):
    tags_words = [ ]
    for sent in corpus.tagged_sents():
        # sent is a list of word/tag pairs
        # add a specific pair START/START at the beginning
        tags_words.append( ("START", "START") )
        # then all the tag/word pairs for the word/tag pairs in the sentence.
        # shorten tags to 2 characters each
        tags_words.extend([ (tag[:2], word) for (word, tag) in sent ])
        # then mark end END/END
        tags_words.append( ("END", "END") )
   
    #corpus_tags = [tag for (tag, word) in tags_words ]
    return tags_words
"""
    function: probDist
        Args:
            corpus

        Returns: probability distribution of the corpus 
"""
def probDist(corpus):
    tags_words  = get_tags(corpus)
    corpus_tags = [tag for (tag, word) in tags_words ]
    # conditional frequency distribution
    cfd_tagwords = nltk.ConditionalFreqDist(tags_words)
    # conditional probability distribution
    cpd_tagwords = nltk.ConditionalProbDist(cfd_tagwords, nltk.MLEProbDist)

    # make conditional frequency distribution of observations:   
    cfd_tags = nltk.ConditionalFreqDist(nltk.bigrams(corpus_tags))   
    cpd_tags = nltk.ConditionalProbDist(cfd_tags, nltk.MLEProbDist)

    return cpd_tagwords, cpd_tags


#################################################################################
# 4a: Print the probability of a Noun(NN) being 'we' is.						#
#     Print the probability of a Verb(VB) being 'like' is.						#
# Hint: The probability of a tag being a word is: PROBABILITY[TAG].prob(word)	#
# I do the first problem for you												#
#################################################################################
def Task4a():
    tagwords, tags = probDist(brown)
    print("The probability of a Noun(PP) being 'I' is", tagwords["PP"].prob("I"))
    print("The probability of a 'VB' following a 'PP' is", tags["PP"].prob("VB"))    

    # YOUR CODE
    print("The probability of a Noun(PP) being 'we' is", tagwords["PP"].prob("we"))
    print("The probability of a Verb(VB) being 'like' is", tagwords["VB"].prob("like"))

Task4a()

#################################################################################################################
# 4b: what is the probability of the tag sequence "PP VB PP NN" for the word sequence "I conduct my conduct"?   #
#     																											#
# Hint: The probability of format "PP VB PP NN" is																#
# P(START) * P(PP|START) * P(I | PP)        *																	#
#            P(VB | PP)  * P(like | VB)     *corpus_tags														#
#            P(PP | VB)  * P(my | PP)       *																	#
#            P(NN | PP)  * P(house | NN)    *																	#
#            P(END | NN)																						#
#################################################################################################################
def Task4b(tag_seq, word_seq):
    tagwords, tags = probDist(brown)

    # YOUR CODE
    tag_list = tag_seq.split(sep=" ")
    word_list = word_seq.split(sep=" ")

    tag_following_tag = 1
    start = tags["START"].prob(tag_list[0])

    last_tag = tag_list[0]
    probability = start 

    for x in range(1, len(tag_list) - 1):
        word_tag = tagwords[tag_list[x]].prob(word_list[x])
        tag_following_tag = tags[last_tag].prob(tag_list[x])

        last_tag = tag_list[x]
        prob_line = word_tag * tag_following_tag
        probability *= prob_line

    end = tags[tag_list[-1]].prob("END")
    probability *= end
    
    print("\n\nThe probability of the tag sequence\n", 
        tag_seq, "\nfor the word sequence\n", 
            word_seq , "\nis:\n" , probability) 

Task4b("PP VB PP NN", "I conduct my conduct")
Task4b("PP VB NN", "I miss pizza")


# Viterbi:
# If we have a word sequence, what is the best tag sequence?
#
# We can determine the probability for a single tag sequence.
# But in order to find the best tag sequence, we need the probability
# for _all_ tag sequence.
# What Viterbi gives us is just a good way of computing all those many probabilities
# as fast as possible.
"""
    function: ViterbiBestTag
        Args:
            distinct_tags: distinct tags of the corpus
            tagwords: list tag words
            tags: list tags
            sentence: a sentence

        Returns: the highest probability with tags of the sentence 
"""

def ViterbiBestTag(distinct_tags, tagwords, tags, sentence):    

    # what is the list of all tags?
    #distinct_tags = set([tag for (tag, word) in get_tags(corpus)])
    #tagwords, tags = probDist(corpus)     
    sentlen = len(sentence)

    # viterbi:
    # for each step i in 1 .. sentlen,
    # store a dictionary
    # that maps each tag X
    # to the probability of the best tag sequence of length i that ends in X
    viterbi = [ ]

    # backpointer:
    # for each step i in 1..sentlen,
    # store a dictionary
    # that maps each tag X
    # to the previous tag in the best tag sequence of length i that ends in X
    backpointer = [ ]

    first_viterbi = { }
    first_backpointer = { }
    for tag in distinct_tags:
        # don't record anything for the START tag
        if tag == "START": continue
        first_viterbi[ tag ] = tags["START"].prob(tag) * tagwords[tag].prob( sentence[0] )
        first_backpointer[ tag ] = "START"

    #print(first_viterbi)
    #print(first_backpointer)
       
    viterbi.append(first_viterbi)
    backpointer.append(first_backpointer)

    currbest = max(first_viterbi.keys(), key = lambda tag: first_viterbi[ tag ])
    #print( "Word", "'" + sentence[0] + "'", "current best two-tag sequence:", first_backpointer[ currbest], currbest)
    # print( "Word", "'" + sentence[0] + "'", "current best tag:", currbest)

    for wordindex in range(1, len(sentence)):
        this_viterbi = { }
        this_backpointer = { }
        prev_viterbi = viterbi[-1]
       
        for tag in distinct_tags:
            # don't record anything for the START tag
            if tag == "START": continue

            # if this tag is X and the current word is w, then
            # find the previous tag Y such that
            # the best tag sequence that ends in X
            # actually ends in Y X
            # that is, the Y that maximizes
            # prev_viterbi[ Y ] * P(X | Y) * P( w | X)
            # The following command has the same notation
            # that you saw in the sorted() command.
            best_previous = max(prev_viterbi.keys(),
                                key = lambda prevtag: \
                prev_viterbi[ prevtag ] * tags[prevtag].prob(tag) * tagwords[tag].prob(sentence[wordindex]))

            # Instead, we can also use the following longer code:
            # best_previous = None
            # best_prob = 0.0
            # for prevtag in distinct_tags:
            #    prob = prev_viterbi[ prevtag ] * cpd_tags[prevtag].prob(tag) * cpd_tagwords[tag].prob(sentence[wordindex])
            #    if prob > best_prob:
            #        best_previous= prevtag
            #        best_prob = prob
            #
            this_viterbi[ tag ] = prev_viterbi[ best_previous] * \
                tags[ best_previous ].prob(tag) * tagwords[ tag].prob(sentence[wordindex])
            this_backpointer[ tag ] = best_previous

        currbest = max(this_viterbi.keys(), key = lambda tag: this_viterbi[ tag ])
        #print( "Word", "'" + sentence[ wordindex] + "'", "current best two-tag sequence:", this_backpointer[ currbest], currbest)
        # print( "Word", "'" + sentence[ wordindex] + "'", "current best tag:", currbest)


        # done with all tags in this iteration
        # so store the current viterbi step
        viterbi.append(this_viterbi)
        backpointer.append(this_backpointer)


    # done with all words in the sentence.
    # now find the probability of each tag
    # to have "END" as the next tag,
    # and use that to find the overall best sequence
    prev_viterbi = viterbi[-1]
    best_previous = max(prev_viterbi.keys(),
                        key = lambda prevtag: prev_viterbi[ prevtag ] * tags[prevtag].prob("END"))

    prob_tagsequence = prev_viterbi[ best_previous ] * tags[ best_previous].prob("END")

    # best tagsequence: we store this in reverse for now, will invert later
    best_tagsequence = [ "END", best_previous ]
    # invert the list of backpointers
    backpointer.reverse()

    # go backwards through the list of backpointers
    # (or in this case forward, because we have inverter the backpointer list)
    # in each case:
    # the following best tag is the one listed under
    # the backpointer for the current best tag
    current_best_tag = best_previous
    for bp in backpointer:
        best_tagsequence.append(bp[current_best_tag])
        current_best_tag = bp[current_best_tag]

    best_tagsequence.reverse()
    #print( "The sentence was:", end = " ")
    #for w in sentence: print( w, end = " ")
    #print("\n")
    #print( "The best tag sequence is:", end = " ")
    #for t in best_tagsequence: print (t, end = " ")
    #print("\n")
    #print( "The probability of the best tag sequence is:", prob_tagsequence)
    best_tags =[]
    for t in best_tagsequence: best_tags.append(t)
    return prob_tagsequence, ' '.join(best_tags)


##########################################################################################
# 4c:																					    #
# what is the best tag sequence of sentence "I love my class" and its probability?		    #
#     																					    #
# Hint: using ViterbiBestTag															    #
##########################################################################################
def Task4c():
    print( "The sentence is: I love my class", end = " ")
    # YOUR CODE
    tagwords, tags = probDist(brown)
    sentence = ["I", "love", "my", "class"]
    distinct_tags = set([tag for (tag, word) in get_tags(brown)])

    probability_value = ViterbiBestTag(distinct_tags, tagwords, tags, sentence)
    print(probability_value)

Task4c()