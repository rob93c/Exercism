def slices(series, length):
	out = []
	if len(series) < length or length < 1:
		raise ValueError("Length argument doesn't fit the series.")
	else:
		for i in range(len(series) - length + 1):
			out.append(series[i:i + length])
		return out
