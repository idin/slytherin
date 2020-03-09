
# The Dictionary class is the same as dict with additional methods

DICT_DIR = dir(dict)

class Dictionary(dict):

	def copy(self):
		return Dictionary(super().copy())

	# the map method allows you to run a function on all values of the dictionary
	def map(self, func, inplace = False):
		if inplace:
			copy = self
		else:
			copy = self.copy()

		try:
			for key in copy:
				copy[key] = func(copy[key])
		except TypeError:
			return False

		if inplace==False:
			return copy

	# based on a solution on stackoverflow:
	# https://stackoverflow.com/questions/12229064/mapping-over-values-in-a-python-dictionary

	@staticmethod
	def from_lists(keys, values = None):
		if values is None:
			values = keys

		return Dictionary(zip(keys, values))

	def __setitem__(self, key, value):
		if key in DICT_DIR:
			raise KeyError(f'key "{key}" is not allowed')
		else:
			super().__setitem__(key, value)

	def __getattribute__(self, item):
		if item in DICT_DIR:
			return super().__getattribute__(item)
		else:
			try:
				return self[item]
			except:
				return super().__getattribute__(item)

	def __dir__(self):
		return super().__dir__() + [str(x) for x in self.keys()]
