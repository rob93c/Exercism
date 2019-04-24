def classify(number):
    if number < 1:
        raise ValueError("The number must be > 0")
    elif get_sum(number) == number:
        return "perfect"
    elif get_sum(number) > number:
        return "abundant"
    elif get_sum(number) < number:
        return "deficient"
    else:
        raise ValueError("Insert a valid number.")


def get_sum(num):
    aliquot = 0
    for i in range(1, num):
        if num % i == 0:
            aliquot += i
    return aliquot
