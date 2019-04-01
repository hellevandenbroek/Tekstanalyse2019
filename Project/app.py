# TODO: make corpus great again. Get 200 tweets from input user
# TODO: treat corpus
# TODO: Ngrams, få dette til å bli riktig
# TODO: poetry generation

import sys
from createCorpus import CreateCorpus
from poetryGenerator import PoetryGenerator
import os
options = ["add account",
           "generate poem",
            "list stored",
           "update corpus",
           "exit application"]


def print_options():
    for option in options:
        capitalized = option.split()
        first_word = ''.join([x.capitalize() for x in capitalized[0]])
        rest = ''.join(capitalized[1:])
        print("\t- {} {}".format(first_word, rest))


def determine_choice(choice):
    for i in range(len(options)):
        option = options[i]
        if choice == option:
            return i
        split_option = option.split()
        for spl in split_option:
            if choice == spl:
                return i
    print("Argument invalid. Try again.")
    return -1


def handle_list():
    files = os.listdir("./Corpus")
    shaved = [x.strip(".txt") for x in files]
    print_accounts(shaved)


def print_accounts(accounts):
    print("Generate poems based on these accounts:")
    for account in accounts:
        print("\t- {}".format(account))


def handle_corpus():
    user = input("Type in a twitter-account you want to generate poetry from: ")
    cp = CreateCorpus(user)
    cp.main()


def handle_update():
    invalid_username = "update_corpus"
    cp = CreateCorpus(invalid_username)


def handle_poem_generation():
    print("From which of your corpus would you like to generate a poem?: ")
    user = input(">")
    print("Would you like the poem to be 'happy' or 'sad'?: ")
    mood = input(">")

    pg = PoetryGenerator(user, mood)
    pg.main()


while True:
    print("\n<~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~>\n What do you want to do?")
    print_options()
    user_choice = input(">")
    chosen_choice = determine_choice(user_choice)
    if chosen_choice != -1:
        # first option
        if chosen_choice == 0:
            handle_corpus()
        if chosen_choice == 1:
            handle_poem_generation()
        if chosen_choice == 2:
            handle_list()
        if chosen_choice == 3:
            handle_update()
        if chosen_choice == 4:
            print("Closed application")
            sys.exit()
