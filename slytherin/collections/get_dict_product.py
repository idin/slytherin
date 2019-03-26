from itertools import product


def get_dict_product(d):
	labels = d.keys()
	value_lists = [d[k] for k in d.keys()]
	value_combinations = product(*value_lists)
	result = [dict(zip(labels, values)) for values in value_combinations]
	return result


