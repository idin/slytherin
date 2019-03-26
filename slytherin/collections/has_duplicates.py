from collections import Counter


def has_duplicates(l):
	"""
	:type l: list
	:rtype: bool
	"""
	if len(l) == 0:
		return False
	else:
		return Counter(l).most_common()[0][1] > 1


def get_duplicates(l):
	"""
	:type l: list
	:rtype: list
	"""
	return [k for k, v in Counter(l).items() if v > 1]


