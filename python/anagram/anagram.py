def find_anagrams(word, candidates):
    result = [i for i in candidates if i.lower() != word.lower(
    ) and sorted(i.lower()) == sorted(word.lower())]
    return result
