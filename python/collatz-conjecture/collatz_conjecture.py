def collatz_steps(number):
    steps = 0
    if number < 1:
    	raise ValueError("Starting number must be positive.")
    else:
    	while not number == 1:
    		if (number % 2) == 0:
    			number /= 2
    			steps += 1
    		else:
    			number = 3 * number + 1
    			steps += 1
    	return steps
