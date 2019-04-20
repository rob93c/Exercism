def find_anagrams(word, candidates):
    result = []
    for i in candidates:
    	if i.lower() != word.lower() and sorted(i.lower()) == sorted(word.lower()):
    		result.append(i)
    return result
