import random

dictionary = {}

def get_dict() -> dict:
    return dictionary

def random_word(length: int = 5) -> str: 
    return random.choice(dictionary[length])

def match_encode(chosen: str, guess: str) -> list:
    res = []
    for (c, g) in zip(chosen, guess):
        if c == g:
            res.append("EXACT_MATCH")
        elif g in chosen:
            res.append("WRONG_PLACE")
        else:
            res.append("NO_MATCH")
        
    return res
    
def __init__() -> None:
    with open("en_US.dic") as f:
        for word in f:
            word = word.rstrip().split('/')[0].upper()
            dictionary[len(word)] = dictionary[len(word)] | {word}
