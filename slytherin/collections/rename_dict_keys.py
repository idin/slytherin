from copy import deepcopy


def rename_dict_keys(dictionary, mapping, recursive=True, raise_error=False):
	"""
	:type dictionary: dict
	:type mapping: dict
	:type recursive: bool
	:type raise_error: bool
	:rtype: dict
	"""
	dictionary = deepcopy(dictionary)

	if isinstance(dictionary, dict):
		for old_key, new_key in mapping.items():
			if old_key in dictionary:
				dictionary[new_key] = dictionary.pop(old_key)
			elif raise_error:
				raise KeyError(f'{old_key} does not exist in dictionary.')
		if recursive:
			for key, value in dictionary.items():
				dictionary[key] = rename_dict_keys(dictionary=value, mapping=mapping)

		return dictionary

	elif isinstance(dictionary, list):
		if recursive:
			return [rename_dict_keys(dictionary=d, mapping=mapping) for d in dictionary]
		else:
			return dictionary

	else:
		return dictionary

