from builtins import property
from .number_part import NumberPart


class FlexibleNumber:
	def __init__(self, parts = [], labels = None, sep = '-'):
		self._parts = parts
		self._sep = sep

		if labels is None:
			labels = list(reversed(range(len(parts))))
		self._labels = labels

		if len(parts) != len(labels):
			raise ValueError(f"parts and labels should be the same length but they are {len(parts)} and {len(labels)} respectively.")

		if len(labels) != len(set(labels)):
			raise ValueError("labels are not unique")


	@property
	def parts(self):
		return self._parts

	@property
	def labels(self):
		return self._labels

	def len(self):
		return len(self._parts)

	def adjust(self):
		for index in reversed(range(self.len())):
			this_part = self.parts[index]
			if index > 0: # there is another element to the left
				left_part = self.parts[index - 1]
				left_part.value += this_part.carry
				this_part.reset_carry()

	def __str__(self):
		return self._sep.join([str(part) for part in self.parts])

	def __repr__(self):
		return ' | '.join([repr(part) for part in self.parts])

	def get(self, label):
		"""
		:type label: str
		:rtype: NumberPart
		"""
		return self.parts[self.labels.index(label)]

	def set(self, value, label):
		self.parts[self.labels.index(label)].value = value
		self.adjust()

	def add(self, value = 0, label = None):
		if label is None:
			label = self.labels[-1]
		self.parts[self.labels.index(label)].value += value
		self.adjust()

	def get_total(self, label = None):
		if label is None:
			last_index = self.len() - 1
		else:
			last_index = self.labels.index(label)

		total = 0
		for i in range(last_index):
			total += self.parts[i].value + self.parts[i].carry
			total *= self.parts[i+1].base
		total += self.parts[last_index].value + self.parts[last_index].carry

		return total

	def same_class(self, other):
		if type(self) != type(other): return False
		if self.labels != other.labels: return False
		for index in range(self.len()):
			if not self.parts[index].same_class(other.parts[index]): return False
		return True

	def __hash__(self):
		return self.get_total()


	def __eq__(self, other):
		if not self.same_class(other):
			return False
		else:
			return self.get_total() == other.get_total()

	def __ne__(self, other):
		return not self.__eq__(other)

	def __gt__(self, other):
		if not self.same_class(other):
			raise TypeError("the other object is a different class or different FlexibleNumber")
		return self.get_total() > other.get_total()

	def __le__(self, other):
		return not self.__gt__(other)

	def __lt__(self, other):
		if not self.same_class(other):
			raise TypeError("the other object is a different class or different FlexibleNumber")
		return self.get_total() < other.get_total()

	def __ge__(self, other):
		return not self.__lt__(other)




	def copy(self):
		parts = [part.copy() for part in self.parts]
		return self.__class__(parts=parts, labels=self.labels, sep=self._sep)

	def __add__(self, other):
		if not self.same_class(other):
			raise TypeError("the other object is a different class or different FlexibleNumber")

		parts = []
		for i in range(self.len()):
			part = self.parts[i] + other.parts[i]
			part.adjust()
			parts.append(part)

		return  self.__class__(parts=parts, labels=self.labels, sep=self._sep)

	def __sub__(self, other):
		if not self.same_class(other):
			raise TypeError("the other object is a different class or different FlexibleNumber")

		parts = []
		for i in range(self.len()):
			part = self.parts[i] - other.parts[i]
			part.adjust()
			parts.append(part)

		return  self.__class__(parts=parts, labels=self.labels, sep=self._sep)


