from data_structures.hashtable import Hashtable


def repeated_word():
     hashtable = Hashtable()

    # Normalize the input string and split it into words
    words = s.lower().split()

    # iterate through the words
    for word in words:

        if hashtable.has(word):
            # since the word is already in the hashtable, it's the repeated word
            return word

        else:
            # add the word to the hashtable with 1 for first occurrence
            hashtable.set(word, 1)

    # if no repeated word was found, return a message
    return "No repeated word found."
