DAYS = [
    "first",
    "second",
    "third",
    "fourth",
    "fifth",
    "sixth",
    "seventh",
    "eighth",
    "ninth",
    "tenth",
    "eleventh",
    "twelfth",
]

GIFTS = [
    "twelve Drummers Drumming",
    "eleven Pipers Piping",
    "ten Lords-a-Leaping",
    "nine Ladies Dancing",
    "eight Maids-a-Milking",
    "seven Swans-a-Swimming",
    "six Geese-a-Laying",
    "five Gold Rings",
    "four Calling Birds",
    "three French Hens",
    "two Turtle Doves",
]


def recite(start, end):
    result = []
    for day in range(start - 1, end):
        nth = DAYS[day]
        gifts_and = " "
        if day:
            gifts_and += ", ".join(GIFTS[len(GIFTS) - day:]) + ", and "
        result.append(
            f"On the {nth} day of Christmas my true love gave to me:"
            f"{gifts_and}a Partridge in a Pear Tree.")
    return result
