#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    wemalo = list(a_dictionary.keys())[0]
    big = a_dictionary[wemalo]
    for bet, bs in a_dictionary.items():
        if bs > big:
            big = bs
            wemalo = bet
    return (wemalo)
