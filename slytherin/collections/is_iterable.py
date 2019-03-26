def is_iterable(obj, include_string=False):
	"""
	:type include_string: bool
	:rtype: bool
	"""
	try:
		iterator = iter(obj)
		return (type(obj) is not str) or include_string
	except TypeError:
		return False


