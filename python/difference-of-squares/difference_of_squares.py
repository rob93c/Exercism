def square_of_sum(count):
    square = 0
    tot = 0
    for num in range(count + 1):
        tot += num
        square = tot * tot
    return square


def sum_of_squares(count):
    tot = 0
    for num in range(count + 1):
        tot += (num * num)
    return tot


def difference(count):
    return square_of_sum(count) - sum_of_squares(count)
