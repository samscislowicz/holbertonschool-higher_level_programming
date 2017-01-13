#!/usr/bin/python3
def best_score(my_dict):
    if my_dict == {} or my_dict is None:
        return None
    bestscore = max(my_dict, key=my_dict.get)
    return bestscore
