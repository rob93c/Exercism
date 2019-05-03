def flatten(iterable):
    result = []
    for i in iterable:
        if type(i) not in (list, tuple):
            if i is not None:
                result.append(i)
        else:
            result.extend(flatten(i))
    return result
