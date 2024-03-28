from data_structures.hashtable import Hashtable

def left_join(synonyms, antonyms):
    joined = []

    sorted_synonyms = sorted(synonyms.items())

    for key, synonym in sorted_synonyms:
        antonym = antonyms.get(key, "NONE")
        joined.append([key, synonym, antonym])

    return joined
