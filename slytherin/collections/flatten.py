def flatten(l):
	"""
	flattens a list
	:param list l:
	:rtype: list
	"""
	flat_list = []
	for item in l:
		if isinstance(item, list):
			flat_list += flatten(item)
		else:
			flat_list.append(item)
	return flat_list
