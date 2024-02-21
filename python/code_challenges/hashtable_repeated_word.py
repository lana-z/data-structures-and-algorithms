from typing import Hashable
import re
from data_structures.hashtable import Hashtable


def first_repeated_word(s):

    # Remove punctuation using regex and then split the string into words
    words = re.sub(r'[^\w\s]', '', s).lower().split()

    hashtable = Hashtable()

    # Normalize the input string and split it into words
    # words = s.lower().split()


    # iterate through the words
    for word in words:

        if hashtable.has(word):
            # since the word is already in the hashtable, it's the repeated word
            return word

        else:
            # add the word to the hashtable with 1 for first occurrence
            hashtable.set(word, 1)

    # if no repeated word was found, return a message
    return None
