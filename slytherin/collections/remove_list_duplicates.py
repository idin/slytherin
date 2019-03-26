def remove_list_duplicates(l):
	used = set()
	unique_list = [x for x in l if x not in used and (used.add(x) or True)]
	return unique_list