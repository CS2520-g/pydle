import random

dictionary = {}
def get_dict():
    return dict

def random_word(length = 5) -> str: 
    return random.choice(dictionary[length])


def __init__():
    with open("en_US.dic") as f:
        for word in f:
            word = word.rstrip().split('/')[0].upper()
            dictionary[len(word)] = dictionary[len(word)] | {word}
