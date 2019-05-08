al1 = "abcdefghijklmnopqrstuvwxyz"
al2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rotate(text: str, key: int) -> str:
    output = ""
    for i in text:
        if i.islower() and i in al1:
            x = al1.index(i)
            output += al1[x + key - len(al1)]
        elif i.isupper() and i in al2:
            x = al2.index(i)
            output += al2[x + key - len(al2)]
        else:
            output += i
    return output
