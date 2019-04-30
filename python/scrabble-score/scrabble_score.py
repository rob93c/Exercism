def score(word):
    up = word.upper()
    count = 0
    for letter in up:
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or \
           letter == 'L' or letter == 'N' or letter == 'R' or letter == 'S' or letter == 'T':
            count += 1
        elif letter == 'D' or letter == 'G':
            count += 2
        elif letter == 'B' or letter == 'C' or letter == 'M' or letter == 'P':
            count += 3
        elif letter == 'F' or letter == 'H' or letter == 'V' or letter == 'W' or letter == 'Y':
            count += 4
        elif letter == 'K':
            count += 5
        elif letter == 'J' or letter == 'X':
            count += 8
        elif letter == 'Q' or letter == 'Z':
            count += 10
        else:
            count += 0
    return count
