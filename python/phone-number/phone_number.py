import re

class Phone(object):
    def __init__(self, phone_number):
        self.phone_number = re.sub("[^0-9]", "", phone_number)
        if len(self.phone_number) < 10:
            raise ValueError("Invalid phone number")
        if len(self.phone_number) > 10:
            if self.phone_number[0] == '1':
                self.phone_number = self.phone_number[1:]
            else:
                raise ValueError("Invalid phone number.")
        if self.phone_number[0] in ['0', '1']  or self.phone_number[3] in ['0', '1']:
            raise ValueError("Invalid phone number.")
        self.number = self.phone_number
        self.area_code = self.phone_number[:3]

    def pretty(self):
        return f"({self.number[:3]}) {self.number[3:6]}-{self.number[6:]}"
