SUBLIST, SUPERLIST, EQUAL, UNEQUAL = range(1, 5)


def check_lists(first_list: str, second_list: str):
    if first_list == second_list:
        return EQUAL
    elif issub(first_list, second_list):
        return SUBLIST
    elif issub(second_list, first_list):
        return SUPERLIST
    else:
        return UNEQUAL


def issub(str1: str, str2: str) -> bool:
    for i in range(len(str2) - len(str1) + 1):
        if str2[i:len(str1) + i] == str1:
            return True
    return False
