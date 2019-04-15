def is_armstrong(number):
    strnum = str(number)
    count = 0
    
    for i in range(len(strnum)):
    	count += int(strnum[i]) ** len(strnum)
    if count == number:
    	return True
    else: 
    	return False
