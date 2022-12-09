#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        for x, y in a_dictionary.items():
            if y == max(a_dictionary.values()):
                return x
