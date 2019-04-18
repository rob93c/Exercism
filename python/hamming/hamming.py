def distance(strand_a, strand_b):
	dist = 0
	if not len(strand_a) == len(strand_b):
		raise ValueError("Invalid strands provided.")
	elif strand_a == strand_b:
		return 0
	else:
		for x in range(len(strand_a)):
			if not strand_a[x] == strand_b[x]:
				dist += 1
			else:
				dist += 0	
		return dist
