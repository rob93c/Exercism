def triplets_with_sum(sum_of_triplet):
    triplets = set()
    for t in triplets_in_range(3, sum_of_triplet):
        if is_triplet(t):
            triplets.add(t)
    return triplets


def triplets_in_range(range_start, range_end):
    for a in range(range_start, range_end // 2):
        for b in range(a + 1, range_end // 2):
            c = range_end - b - a
            if a < b < c:
                yield (a, b, c)


def is_triplet(triplet):
    return sorted(triplet)[0] ** 2 + sorted(triplet)[1] ** 2 == sorted(triplet)[2] ** 2
