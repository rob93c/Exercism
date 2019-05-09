class Clock(object):

    def __init__(self, hour, minute):
        remainder = minute // 60
        self.minute = minute % 60
        self.hour = (hour + remainder) % 24

    def __repr__(self):
        if self.hour == 0 and self.minute == 0:
            return f"{self.hour}0:{self.minute}0"
        elif self.hour < 10 and self.minute > 9:
            return f"0{self.hour}:{self.minute}"
        elif self.hour > 9 and self.minute == 0:
            return f"{self.hour}:{self.minute}0"
        elif self.hour < 10 and self.minute == 0:
            return f"0{self.hour}:{self.minute}0"
        elif self.hour == 0 and self.minute < 10:
            return f"{self.hour}0:0{self.minute}"
        elif self.hour > 9 and self.minute < 10:
            return f"{self.hour}:0{self.minute}"
        elif self.hour < 10 and self.minute < 10:
            return f"0{self.hour}:0{self.minute}"
        else:
            return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        return Clock(self.hour, self.minute + minutes)

    def __sub__(self, minutes):
        return Clock(self.hour, self.minute - minutes)
