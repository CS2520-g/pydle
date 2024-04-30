import random
from enum import Enum

class CharacterMatch(Enum):
    FULL_MATCH = 1
    WRONG_PLACE = 2
    NO_MATCH = 3

dictionary = {}

minsize = 1
maxsize = 1

with open("en_US.dic") as f:
    for word in f:
        word = word.rstrip().split('/')[0].upper()
        if len(word) in dictionary:
            dictionary[len(word)].append(word)
        else:
            dictionary[len(word)] = [word]
        maxsize = max(maxsize, len(word))

def wordrange() -> tuple[int, int]:
    return (minsize, maxsize)

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

def match_encode(chosen: str, guess: str) -> list[CharacterMatch]:
    chosen = chosen.upper()
    guess = guess.upper()
    chosen_counts = char_counts(chosen)

    res = []
    for (c, g) in zip(chosen, guess):
        if c == g:
            res.append(CharacterMatch.FULL_MATCH)
        elif g in chosen_counts:
            res.append(CharacterMatch.WRONG_PLACE)
            chosen_counts[g] -= 1
            if chosen_counts[g] == 0:
                del chosen_counts[g]
        else:
            res.append(CharacterMatch.NO_MATCH)
        
    return res

def isword(word: str) -> bool:
    return word in dictionary