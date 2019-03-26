# TODO: make corpus great again. Get 200 tweets from input user
# TODO: treat corpus
# TODO: Ngrams, få dette til å bli riktig
# TODO: poetry generation


from twitterCorpus import CorpusGenerator
from poetryGenerator import PoetryGenerator

options = ["add account", "generate poem"]


def print_options():
    for option in options:
        print("- {}".format(option))


def determine_choice(choice):
    for i in range(len(options)):
        option = options[i]
        split_option = option.split()
        for spl in split_option:
            if choice == spl:
                return i
    print("Argument invalid. Try again.")
    return -1


print("<~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~ ~~>")
print("What do you want to do?")
print_options()
user_choice = input(">")
chosen_choice = determine_choice(user_choice)
if chosen_choice != -1:
    # first option
    if chosen_choice == 0:
        user = input("Type in a twitter-account you would want to make a corpus from: ")
        cp = CorpusGenerator(user)
        cp.save_to_file()
    if chosen_choice == 1:
        user = input("From which of your corpus would you like to generate a poem?: ")
        hello = PoetryGenerator(user)





