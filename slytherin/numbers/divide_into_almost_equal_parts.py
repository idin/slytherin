def divide_into_almost_equal_parts(number, by):
	"""
	:type number: int
	:type by: int
	:rtype: list[int]
	"""

	return [
		number // by + (1 if x < number % by else 0)
		for x in range(by)
	]
