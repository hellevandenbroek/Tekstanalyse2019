from nltk.corpus import names
import nltk
import random
from nltk.classify import apply_features

# Set up classifier for use in task
labeled_names = ([(name, 'male') for name in names.words('male.txt')]
    + [(name, 'female') for name in names.words('female.txt')] 
)
random.shuffle(labeled_names)

# Extracting features from a given name
def gender_features(name):
    return {'suffix1': name[-1],
            'suffix2': name[-2],
            'length-of-name': len(name),
            'first-letter': name[0]
        }

# using partition all names
train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n, gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n, gender) in test_names]


def extract_gender(classifier, name):
    gender = classifier.classify(gender_features(name))
    print("\nExtracting gender from name:", name, "\n Gender:", gender)

def print_accuracy(classifier_name ,set_name, classifier, word_set):
    accuracy = nltk.classify.accuracy(classifier, word_set)
    print("\nAccuracy for gender classifier ({}) based on {} set: {}".format(classifier_name, set_name, accuracy))


# Used for finding errors in a classifier
def find_name_errors(classifier, names):
    errors = []
    for (name, tag) in names:
        guess = classifier.classify(gender_features(name))
        if guess != tag:
            errors.append((tag, guess, name))
    return errors


def print_name_errors(errors):
    for (tag, guess, name) in sorted(errors):
        print('correct={:<8} guess={:<8} name={:<30}'.format(tag, guess, name))


# Naive Bayes
def start_bayes_classifier(train): # train_set
    return nltk.NaiveBayesClassifier.train(train)


# DecisionTreeClassifier
def start_decision_tree_classifier(train):
    return nltk.DecisionTreeClassifier.train(train)


# Maximum Entropy
def start_maxent_classifier(train):
    return nltk.MaxentClassifier.train(train, trace=0, max_iter=30)


# starting the three classifiers
NVclassifier = start_bayes_classifier(train_set)
DTClassifier = start_decision_tree_classifier(train_set)
MEClassifier = start_maxent_classifier(train_set)

# printing the accuracies
print_accuracy("NB", "test", NVclassifier, test_set)
print_accuracy("DT", "test", DTClassifier, test_set)
print_accuracy("ME", "test", MEClassifier, test_set)