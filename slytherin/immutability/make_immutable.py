from .ImmutableDictionary import ImmutableOrderedDict, ImmutableDictionary
from ..hash import hash_object

from datetime import datetime
from inspect import isfunction
from collections import OrderedDict
from functools import wraps
from copy import deepcopy

IMMUTABLE_TYPES = frozenset({
	type(None),
	bool,
	int,
	float,
	complex,
	str,
	bytes,
	tuple,
	datetime,
	ImmutableDictionary,
	ImmutableOrderedDict
})

def is_immutable(obj):
	"""
	Determine whether a thing is immutable
	:param value obj: a Python value (object or primitive)
	:returns true if the value is known to be immutable
	:rtype bool
	"""

	return (
		any([
			isinstance(obj, t)
			for t in IMMUTABLE_TYPES.union(frozenset({Immutable, frozenset}))
		]) or
		isfunction(obj)
	)

class Immutable(object):
	"""
		A wrapper for arbitrary Python objects,
		that protects against attribute mutation
		Warning: `freezemethod` and `freezeobject` perform a `deepcopy`
		of the object's attributes upon each method call in order to
		test whether the method call would modify the object.
		The attribute copy may use a significant amount of memory.
		To save memory, model data with structures designed to be immutable,
		such as tuples, frozensets, ImmutableDictionaries, etc.
	"""

	def __init__(self, value):
		"""
			Construct a immutable object
			:param value value: a Python object
			:returns a immutable version of the object
		"""

		self._original_object = value

	def __hashkey__(self):
		return 'immutable', self.__class__.__name__, self._original_object

	@property
	def original_object(self):
		return deepcopy(self._original_object)

	def __getattribute__(self, name):
		"""
			Override attribute getters,
			returning immutable versions of each attribute
			:param str name: an attribute name
			:returns value: a wrapped version of the attribute
		"""
		if name in ['_original_object', 'original_object', '__getstate__', '__setstate__', '__call__', '__hashkey__']:
			return super(Immutable, self).__getattribute__(name)
		if name == '__class__':
			return getattr(self._original_object, name)

		attribute = getattr(self._original_object, name)

		# protect methods from mutation
		if callable(attribute) and not isfunction(attribute):
			#print(f'"{name}" is callable, making function immutable', end=' ... ')
			return make_function_immutable(self._original_object, name)
		# protect non-method attributes from mutation
		else:
			#print(f'"{name}" is not callable, making immutable', end=' ... ')
			return make_immutable(attribute)

	def __setattr__(self, name, value):
		"""
			Override attribute setters,
			preventing attribute mutation
			:param str name: an attribute name
			:param value value: a value for the attribute to take
			:raises LiquidNitrogenException in most cases
		"""

		if name == '_original_object':
			super(Immutable, self).__setattr__('_original_object', value)
		else:
			print(f'Cannot alter attribute {name} of object {self} of type {type(self)}')
			raise AttributeError(f'Cannot alter attribute {name} of object {self} of type {type(self)}')

	def __call__(self, *args, **kwargs):
		"""
			Forwards method calls to the wrapped object
			:param list args: any positional call arguments
			:param dict kwargs: any named call arguments
			:returns value: the return value of the wrapped method call
			:raises LiquidNitrogenException if call would modify this object
		"""
		return self._original_object.__call__(*args, **kwargs)

	def __repr__(self):
		"""
			Forwards string representation calls to the wrapped object
			:returns str: a string representation of the wrapped object
		"""

		return self._original_object.__repr__()

	def __getitem__(self, item):
		return self._original_object[item]

	def __dir__(self):
		return dir(self._original_object)

	def __getstate__(self):
		return self._original_object

	def __setstate__(self, state):
		self._original_object = state

def make_function_immutable(obj, name):
	"""
		Create an immutable version of a method,
		that detects when a call would modify the object,
		and instead raises LiquidNitrogenException
		Warning: `freezemethod` and `freezeobject` perform a `deepcopy`
		of the object's attributes upon each method call in order to
		test whether the method call would modify the object.
		The attribute copy may use a significant amount of memory.
		To save memory, model data with structures designed to be immutable,
		such as tuples, frozensets, ImmutableDictionaries, etc.
		:param object obj: an object
		:param str name: a method to wrap on the object
		:returns method: a wrapped method that protects against mutation
	"""

	obj_copy_hash = hash_object(obj)
	method_copy = getattr(obj, name)

	@wraps(method_copy)
	def protected_method(*args, **kwargs):
		result = method_copy(*args, **kwargs)

		# Has the copy mutated compared to the original?
		if obj_copy_hash == hash_object(obj):
			return result
		else:
			print(f'immutable method call {name} with arguments {args} {kwargs} would mutate {obj}')
			raise RuntimeError(f'immutable method call {name} with arguments {args} {kwargs} would mutate {obj}')

	return protected_method


def make_immutable(obj):
	"""
		Given a Python value, return an immutable version of the value.
		Natively immutable values such as tuples, immutablesets, and ImmutableDictionaries
		are simply returned as-is.
		Methods and objects are wrapped to raise LiquidNitrogenExceptions
		on attempts to set attributes or call methods
		that would mutate the objects.
		Warning: `freezemethod` and `freezeobject` perform a `deepcopy`
		of the object's attributes upon each method call in order to
		test whether the method call would modify the object.
		The attribute copy may use a significant amount of memory.
		To save memory, model data with structures designed to be immutable,
		such as tuples, immutablesets, ImmutableDictionaries, etc.
		:param value obj: a Python value (object or primitive)
		:returns a immutable version of the value
	"""

	if is_immutable(obj):
		return obj
	elif isinstance(obj, list):
		return tuple(obj)
	elif isinstance(obj, set):
		return frozenset(obj)
	elif isinstance(obj, OrderedDict):
		return ImmutableOrderedDict(obj)
	elif isinstance(obj, dict):
		return ImmutableDictionary(obj)
	else:
		return Immutable(obj)
