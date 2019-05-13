def sum(l):
	"""
	:type l: list
	"""
	if len(l) == 1:
		return l[0]
	elif len(l) == 2:
		return l[0] + l[1]
	elif len(l) > 2:
		middle = len(l) // 2
		return sum(l[:middle]) + sum(l[middle:])
	else:
		raise TypeError('list is empty!')
