def proteins(strand):
    output = []
    temp_str = []
    index = 0
    for x in strand:
    	temp_str = strand[index:index+3]
    	if temp_str == "AUG":
    		output.append('Methionine')
    	elif temp_str == "UUU" or temp_str == "UUC":
    		output.append('Phenylalanine')
    	elif temp_str == "UUA" or temp_str == "UUG":
    		output.append('Leucine')
    	elif temp_str == "UCU" or temp_str == "UCC" or temp_str == "UCA" or temp_str == "UCG":
    		output.append('Serine')
    	elif temp_str == "UAU" or temp_str == "UAC":
    		output.append('Tyrosine')
    	elif temp_str == "UGU" or temp_str == "UGC":
    		output.append('Cysteine')
    	elif temp_str == "UGG":
    		output.append('Tryptophan')
    	else:
    		return output
    	index = index + 3
    return output	
