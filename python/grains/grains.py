def on_square(integer_number):
    if integer_number > 64 or integer_number < 1:
        raise ValueError("There are only 64 squares")
    else:
        return 2 ** (integer_number - 1)


def total_after(integer_number):
    total = 0
    if integer_number > 64 or integer_number < 1:
        raise ValueError("There are only 64 squares")
    else:
        for num in range(1, 65):
            total += on_square(num)
    return total
