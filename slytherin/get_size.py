from collections import Mapping, Iterable
from sys import getsizeof

def deep_getsizeof(o, ids):
	"""Find the memory footprint of a Python object
	This is a recursive function that rills down a Python object graph
	like a dictionary holding nested ditionaries with lists of lists
	and tuples and sets.
	The sys.getsizeof function does a shallow size of only. It counts each
	object inside a container as pointer only regardless of how big it
	really is.
	:param o: the object
	:param ids:
	:return:
	"""
	ids = ids or set()
	d = deep_getsizeof
	if id(o) in ids:
		return 0

	r = getsizeof(o)
	ids.add(id(o))

	if isinstance(o, str):
		return r

	if isinstance(o, Mapping):
		return r + sum(d(k, ids) + d(v, ids) for k, v in o.items())

	if isinstance(o, Iterable):
		return r + sum(d(x, ids) for x in o)
	# source: https://github.com/the-gigi/deep/blob/master/deeper.py#L80
	return r

def get_size(obj, exclude_objects=None):
	""" Find the memory footprint of a Python object recursively
	:param object obj:
	:rtype: int
	"""
	exclude_objects = exclude_objects or []
	return deep_getsizeof(o=obj, ids=set([id(x) for x in exclude_objects]))