from collections import Counter
from re import findall


def word_count(phrase):
    counts = dict()
    words = phrase\
        .strip("!&@$%^&.")\
        .lower()\
        .replace(",", " ")\
        .replace("_", " ")\
        .replace(":", "")\
        .replace("\"", "")\
        .replace(".", "")\
        .split()

    for word in words:
        if word.strip("'") in counts:
            counts[word.strip("'")] += 1
        else:
            counts[word.strip("'")] = 1
    return counts
