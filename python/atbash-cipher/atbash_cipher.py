import re

txt = list("abcdefghijklmnopqrstuvwxyz")
cip = list("zyxwvutsrqponmlkjihgfedcba")


def encode(plain_text: str) -> str:
    output = ""
    for i in re.sub("[^0-9a-zA-Z]", "", plain_text.lower()):
        if i.isdigit():
            output += i
        else:
            index = txt.index(i)
            output += cip[index]
    return space(output)


def decode(ciphered_text: str) -> str:
    output = ""
    for i in re.sub("[^0-9a-zA-Z]", "", ciphered_text.lower()):
        if i.isdigit():
            output += i
        else:
            index = cip.index(i)
            output += txt[index]
    return output


def space(string: str) -> str:
    return " ".join(string[i:i + 5] for i in range(0, len(string), 5))
