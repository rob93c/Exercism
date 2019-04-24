def hey(phrase: str) -> str:
    if phrase == "" or phrase.isspace():
        return "Fine. Be that way!"
    else:
        phrase = phrase.replace(" ", "")
        if phrase.isupper() and phrase[-1] == "?":
            return "Calm down, I know what I'm doing!"
        elif phrase.isupper():
            return "Whoa, chill out!"
        elif phrase[-1] == "?":
            return "Sure."
        else:
            return "Whatever."
