def find_duplicates(items):
	"""
	:type items: list
	:rtype: list
	"""
	seen = {}
	dupes = []

	for x in items:
		if x not in seen:
			seen[x] = 1

		else:
			if seen[x] == 1:
				dupes.append(x)
			seen[x] += 1

	return dupes
