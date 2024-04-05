import random

dictionary = {}

def get_dict() -> dict:
    return dictionary

def random_word(length: int = 5) -> str: 
    return random.choice(dictionary[length])

def char_counts(word: str) -> dict:
    d = {}
    for c in word:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    return d

def match_encode(chosen: str, guess: str) -> list:
    chosen = chosen.upper()
    guess = guess.upper()
    chosen_counts = char_counts(chosen)

    res = []
    for (c, g) in zip(chosen, guess):
        if c == g:
            res.append("EXACT_MATCH")
        elif g in chosen_counts:
            res.append("WRONG_PLACE")
            chosen_counts[g] -= 1
            if chosen_counts[g] == 0:
                del chosen_counts[g]
        else:
            res.append("NO_MATCH")
        
    return res
    
def __init__() -> None:
    with open("en_US.dic") as f:
        for word in f:
            word = word.rstrip().split('/')[0].upper()
            dictionary[len(word)] = dictionary[len(word)] | {word}
