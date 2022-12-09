#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        mx = max(a_dictionary.values())
        for x, y in a_dictionary.items():
            if y == mx:
                return x
