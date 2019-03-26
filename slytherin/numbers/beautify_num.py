def beautify_num(x):
	"""
	:type x: float or int
	:rtype: str
	"""
	if abs(x) >= 100 or abs(x) <= 0.01:
		value_str = "{:.2e}".format(x)
	elif abs(x) >= 1:
		value_str = "{:.3f}".format(x)
	elif abs(x) >= 0.1:
		value_str = "{:.4f}".format(x)
	else:
		value_str = "{:.4f}".format(x)
	return value_str


