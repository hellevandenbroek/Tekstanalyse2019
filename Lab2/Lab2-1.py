import nltk
from nltk.corpus import brown

tags = brown.tagged_words(categories="news")

cfd = nltk.ConditionalFreqDist(tags)

cond = cfd.conditions()


# a
def find_most_frequent_tag(tagged_words):
    return nltk.FreqDist(tag for (word, tag) in tagged_words) # TODO hvis riktig

# b
def find_words_with_min_num_tags(amount):
    singular_tag = len([cond for cond in cond if len(cfd[cond]) == 1])    
    return len(cond) - singular_tag # 1723

# c
def find_percentage_of_words():
    num = find_words_with_min_num_tags(2)
    
    return  num / len(cond)  # check if correct

# d
def find_greatest_num_distinct_words():
    # TODO Find the 10 words with the greatest number of distinct tags.  
    # Print these words with their tags.
    foo = 'bar'
    distinct_tags = 1
    while True:
        x = find_words_with_min_num_tags(distinct_tags):
        # find 10, then break
        


# e
def print_sentences_from_greatest():
    # TODO For the word with the greatest number of distinct tags, 
    # print out sentences from theBrown Corpuscontaining the word, 
    # one for each possible tag.
    foo = 'bar'

print(find_percentage_of_words())

print("\n~~~~ENDED~~~~")
