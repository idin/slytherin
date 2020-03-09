def multiply_dictionary(dictionary, key, values):
	"""
	:type dictionary: dict
	:type key: str
	:type values: list
	:rtype: list[dict]
	"""
	result = []
	if not isinstance(values, (list, tuple)):
		values = [values]

	for value in values:
		new_d = dictionary.copy()
		new_d[key] = value
		result.append(new_d)
	return result


def create_grid(dictionary):
	"""
	creates a list of dictionaries with all combinations of key-values
	create_grid({'a': [1,2,3], 'b': [10, 20]}) produces:
	[{'a': 1, 'b': 10}, {'a': 1, 'b': 20}, {'a': 2, 'b': 10}, {'a': 2, 'b': 20}, {'a': 3, 'b': 10}, {'a': 3, 'b': 20}]
	:param dict[str, list] dictionary: a dictionary of lists of parameter values
	:rtype: list[dict[str,]]
	"""
	result = [{}]
	for key, values in dictionary.items():
		new_result = []
		for dictionary in result:
			new_result += multiply_dictionary(dictionary=dictionary, key=key, values=values)
		result = new_result
	return result
