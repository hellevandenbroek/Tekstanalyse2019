import nltk

from nltk.book import text9

def find_sentence_with_word(word):
    index = text9.index(word)

    # Finding the dot(".") after the key word
    after_index_value = index
    for word in text9[index:]:
        if word != ".":
            after_index_value += 1
        else:
            break


    # Finding the first dot prior to the key word, 
    # in the sequence.
    before_index_value = index
    for word in text9[index::-1]:
        if word != ".":
            before_index_value -= 1
        else:
            break
    
    whole_sentence = text9[before_index_value + 1:after_index_value + 1]
    return ' '.join(whole_sentence)

received_sentence = find_sentence_with_word("sunset")

print(received_sentence)



