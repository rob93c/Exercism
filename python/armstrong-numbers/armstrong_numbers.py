def is_armstrong(number):
    strnum = str(number)
    count = 0
    for i in strnum:
        count += int(i) ** len(strnum)
    if count == number:
        return True
    else:
        return False
