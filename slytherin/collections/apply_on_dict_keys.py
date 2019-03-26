from copy import deepcopy


def apply_on_dict_keys(dictionary, func, recursive=True):
	"""
		:type dictionary: dict
		:type func: callable
		:rtype: dict
		"""
	dictionary = deepcopy(dictionary)
	if isinstance(dictionary, dict):

		keys = list(dictionary.keys())
		for old_key in keys:

			new_key = func(old_key)
			old_value = dictionary.pop(old_key)
			if recursive:
				new_value = apply_on_dict_keys(dictionary=old_value, func=func, recursive=recursive)
			else:
				new_value = old_value
			dictionary[new_key] = new_value

		return dictionary

	elif isinstance(dictionary, list):
		if recursive:
			return [apply_on_dict_keys(dictionary=d, func=func, recursive=recursive) for d in dictionary]
		else:
			return dictionary

	else:
		return dictionary




