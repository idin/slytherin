def cross_two_lists(l1, l2):
	"""
	:rtype: list[tuple]
	"""
	return [(x, y) for x in l1 for y in l2]


def cross_lists(*args):
	"""
	:rtype: list[tuple]
	"""
	if len(args) == 2:
		return cross_two_lists(args[0], args[1])
	elif len(args) > 2:
		result = cross_lists(cross_two_lists(args[0], args[1]), *args[2:])
		return [(x[0][0], x[0][1], *x[1:]) for x in result]
	elif len(args) == 1 and isinstance(args[0], (list, tuple)):
		return cross_lists(*args[0])
