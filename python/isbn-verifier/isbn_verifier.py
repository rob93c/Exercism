import re

def verify(isbn):
    string = undasher(isbn)
    tot = 0
    count = 10
    if not len(string) == 10 or not re.match(r"^[0-9]{9}[0-9|X]{1}$", string):
    	return False
    else:
    	for ch in string:
    		if ch == "X":
    			ch = 10
    		tot += int(ch) * count
    		count -= 1
    	return (tot % 11) == 0

def undasher(code):
	return code.replace("-", "")
