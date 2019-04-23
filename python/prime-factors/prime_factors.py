def prime_factors(natural_number):
    i = 2
    result = []
    num = natural_number
    while num != 1:
        if num % i == 0:
            result.append(i)
            num /= i
        else:
            i += 1
    return result
