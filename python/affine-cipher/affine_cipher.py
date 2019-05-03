import re
from math import gcd

alpha = list("abcdefghijklmnopqrstuvwxyz")
m = len(alpha)


def encode(plain_text: str, a: int, b: int) -> str:
    output = ""
    validate_key(a)
    for i in re.sub("[^0-9a-zA-Z]", "", plain_text.lower()):
        if i.isdigit():
            output += i
        else:
            x = alpha.index(i)
            output += alpha[(a * x + b) % m]
    return space(output)


def decode(ciphered_text: str, a: int, b: int) -> str:
    output = ""
    inv = mmi(a, m)
    validate_key(a)
    for i in re.sub("[^0-9a-zA-Z]", "", ciphered_text.lower()):
        if i.isdigit():
            output += i
        else:
            y = alpha.index(i)
            output += alpha[(inv * (y - b)) % m]
    return output


def space(string: str) -> str:
    return " ".join(string[i:i + 5] for i in range(0, len(string), 5))


def validate_key(a: int):
    if gcd(a, m) != 1:
        raise ValueError("Error: a and m must be coprime.")


def mmi(a: int, m: int) -> int:
    for n in range(m):
        if (a * n) % m == 1:
            return n
