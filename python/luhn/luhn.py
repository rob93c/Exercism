import re


class Luhn(object):

    def __init__(self, card_num):
        self.card_num = self.unspace(card_num)

    def is_valid(self) -> bool:
        new_int = 0
        tot = 0
        if len(self.card_num) <= 1 or not self.card_num.isdecimal():
            return False
        else:
            return self.total(self.double(self.card_num)) % 10 == 0

    @staticmethod
    def double(card_num: str) -> str:
        func = lambda n: str(2 * n) if n * 2 < 10 else str(n * 2 - 9)
        return ''.join(func(int(char))
                       if n % 2 == 1 else char
                       for n, char in enumerate(card_num[::-1]))[::-1]

    @staticmethod
    def total(string: str) -> int:
        return sum(int(char)
                   for char in string)

    @staticmethod
    def unspace(card_num: str) -> str:
        return ''.join(part.strip()
                       for part in card_num.split())
