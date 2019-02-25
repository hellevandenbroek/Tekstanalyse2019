from nltk.corpus import names
import nltk
import random
from nltk.classify import apply_features

# Set up classifier for use in task
labeled_names = ([(name, 'male') for name in names.words('male.txt')]
    + [(name, 'female') for name in names.words('female.txt')] 
)
random.shuffle(labeled_names)


def gender_features(word):
    return {'last-letter': word[-1],
            'length-of-name': len(word),
            'first-letter': word[0]
            }


# using apply_features
train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]


classifier = nltk.NaiveBayesClassifier.train(train_set)

# Classifier is up. Now for testing

male_name = 'Neo'
female_name = 'Trinity'

neo = classifier.classify(gender_features(male_name))

trinity = classifier.classify(gender_features(female_name))

print("\nExtracting gender from name:", male_name, "\n Gender:", neo)
print("\nExtracting gender from name:", female_name, "\n Gender:", trinity)

dev_accuracy = nltk.classify.accuracy(classifier, devtest_set)
print("\nAccuracy for gender classifier based on dev set: ", dev_accuracy)


# printing information
classifier.show_most_informative_features(10)

def find_errors(names):
    errors = []
    for (name, tag) in names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
    return errors


for (tag, guess, name) in sorted(find_errors(devtest_names)):
    print('correct={:<8} guess={:<8} name={:<30}'.format(tag, guess, name))

test_accuracy = nltk.classify.accuracy(classifier, test_set)
print("Accuracy for gender classifier based on test set: ", test_accuracy)