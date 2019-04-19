def is_equilateral(sides):
    if sides[0] + sides[1] <= sides[2] \
            or sides[2] + sides[1] <= sides[0] \
            or sides[0] + sides[2] <= sides[1]:
        return False
    elif sides[0] == sides[1] and sides[0] == sides[2]:
        return True
    else:
        return False


def is_isosceles(sides):
    if sides[0] + sides[1] <= sides[2] \
            or sides[2] + sides[1] <= sides[0] \
            or sides[0] + sides[2] <= sides[1]:
        return False
    elif sides[0] == sides[1] \
            and sides[0] == sides[2]:
        return True
    elif sides[0] == sides[1] \
            and not sides[0] == sides[2]:
        return True
    elif sides[0] == sides[2] \
            and not sides[0] == sides[1]:
        return True
    elif sides[2] == sides[1] \
            and not sides[2] == sides[0]:
        return True
    else:
        return False


def is_scalene(sides):
    if sides[0] + sides[1] <= sides[2] \
            or sides[2] + sides[1] <= sides[0] \
            or sides[0] + sides[2] <= sides[1]:
        return False
    elif not sides[0] == sides[1] \
            and not sides[0] == sides[2] \
            and not sides[2] == sides[1]:
        return True
    else:
        return False
