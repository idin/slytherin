import hashlib
import base64, base32hex


def make_hashable(obj):
	try:
		return make_hashable(obj.__hashkey__())
	except AttributeError:
		if isinstance(obj, (tuple, list)):
			return tuple((make_hashable(e) for e in obj))

		if isinstance(obj, dict):
			return tuple(sorted((k,make_hashable(v)) for k,v in obj.items()))

		if isinstance(obj, (set, frozenset)):
			return tuple(sorted(make_hashable(e) for e in obj))

		return obj


def hash_dictionary(dictionary, simplify=False, base=64):
	"""
	:type dictionary: dict
	:rtype: str
	"""
	if simplify:
		new_dict = {
			k: (v if isinstance(v, (int, float, str)) else str(v))
			for k, v in dictionary.items()
		}

	else:
		new_dict = {
			k: (v if isinstance(v, (int, float, str)) else hash_object(obj=v, base=base))
			for k, v in dictionary.items()
		}

	return str(set(new_dict.items()))


def hash_object(obj, base=64):
	hash_maker = hashlib.sha256()
	hash_maker.update(repr(make_hashable(obj)).encode())
	if base==64:
		return base64.b64encode(hash_maker.digest()).decode()
	elif base==32:
		return base32hex.b32encode(hash_maker.digest()).replace('=', '-')
	else:
		raise ValueError(f'base{base} is unknown!')
