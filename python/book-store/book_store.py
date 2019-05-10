def calculate_total(books: list) -> int:
    count = [books.count(x) for x in set(books)]
    return len(books) * 800 - max([discount(count, i) for i in range(1, 6)])


def discount(count_list: list, upperbound: int) -> int:
    discount = {1: 0.00, 2: 0.05, 3: 0.10, 4: 0.20, 5: 0.25}
    result = 0
    _l = min(len(count_list), upperbound)
    _sorted = sorted(count_list, reverse=True)
    while _l > 0:
        result += 800 * discount[_l] * _l
        for i, x in enumerate(_sorted[:_l]):
            _sorted[i] = x - 1
        _l = min(len([x for x in _sorted if x > 0]), upperbound)
        _sorted = sorted(_sorted, reverse=True)
    return int(result)
