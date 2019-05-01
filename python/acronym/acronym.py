def abbreviate(words):
    lst = words.upper().replace("_", "").replace(
        "-", " ").replace("  ", "").split(" ")
    string = ""
    for word in lst:
        string += word[0]
    return string
