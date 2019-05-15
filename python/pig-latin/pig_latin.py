import re


def translate(text: str) -> str:
    words = text.split()
    res = ""
    for word in words:
        if res != "":
            res += " "
        res += translateWord(word)
    return res


def translateWord(word: str) -> str:
    pattern1 = re.compile("[aeiou]")
    pattern2 = re.compile("xr")
    pattern3 = re.compile("yt")
    pattern4 = re.compile("sch")
    pattern5 = re.compile("thr")
    pattern6 = re.compile("th")
    pattern7 = re.compile("qu")
    pattern8 = re.compile("ch")
    pattern9 = re.compile("y")

    if pattern1.match(word) != None or pattern2.search(word, 0) != None or pattern3.search(word, 0, 2) != None:
        return word + "ay"
    elif pattern4.search(word, 0) != None or pattern5.search(word, 0) != None or pattern7.search(word, 1) != None:
        return word[3:] + word[:3] + "ay"
    elif pattern6.search(word, 0) != None or pattern7.search(word, 0) != None or pattern8.search(word, 0) != None \
            or (pattern1.match(word) == None and pattern1.search(word, 1) == None and pattern9.search(word, 2) != None):
        return word[2:] + word[:2] + "ay"
    elif len(word) == 2 and pattern9.search(word, 1) != None:
        return "".join(reversed(word)) + "ay"
    elif pattern1.match(word) == None:
        return word[1:] + word[:1] + "ay"
    else:
        raise ValueError("text must be a string.")
