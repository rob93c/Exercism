import re


class Luhn(object):

    def __init__(self, card_num):
        self.card_num = card_num

    def is_valid(self) -> bool:
        new_int = 0
        tot = 0
        num = re.sub("[^0-9]", "", self.card_num)
        if len(num) <= 1:
            return False
        else:
            for i in range(len(num) - 2, - 1, - 2):
                if int(num[i]) < 5:
                    new_int = int(num[i]) * 2
                    num = num[:i] + str(new_int) + num[i + 1:]
                else:
                    new_int = int(num[i]) * 2 - 9
                    num = num[:i] + str(new_int) + num[i + 1:]
                for x in num:
                    tot += int(x)
            return tot % 10 == 0
