from builtins import property
from math import log10


class NumberPart:
	def __init__(self, value= 0, base=10, start=0, digits=None):

		if type(base) is not int and base is not None: raise TypeError("base should be int or None")
		if type(value) is not int: raise TypeError("value should be int")
		if type(start) is not int: raise TypeError("start should be int")

		self._base=base
		self._value=value
		self._start=start

		if digits is None:
			if self.base is None:
				self._digits=1
			else:
				self._digits=int(log10(self.base + self.start - 1))+1
		else:
			if type(digits) is not int: raise TypeError("digits should be int")
			self._digits = digits

		self._carry=0
		self.adjust()

	def adjust(self):
		if self.base is not None:
			self._carry += (self._value - self._start) // self._base
			self._value = (self._value - self._start) % self._base + self._start

	@property
	def base(self):
		return self._base

	@property
	def value(self):
		return self._value

	@property
	def start(self):
		return self._start

	@property
	def carry(self):
		return self._carry

	@property
	def digits(self):
		return self._digits

	@value.setter
	def value(self, value):
		if type(value) is not int: raise TypeError("value should be int")
		self._value=value
		if self.base is not None:
			if self._value < self.start or self._value > self.base - self.start:
				self.adjust()

	def reset_carry(self):
		self._carry=0

	def __repr__(self):
		if self.start==0:
			result = f"{self.value} carry:{self.carry} base:{self.base}"
		else:
			result = f"{self.value}(start={self.start}) carry:{self.carry} base:{self.base}"
		return result

	def __str__(self):
		if self.base is not None:
			return str(self.value + self.carry * self.base).zfill(self.digits)
		else:
			return str(self.value).zfill(self.digits)

	def copy(self):
		the_copy=self.__class__(value=self.value, base=self.base, start=self.start, digits=self.digits)
		the_copy._carry=self.carry
		return the_copy

	def same_class(self, other):
		if type(self) != type(other): return False
		if self.base != other.base: return False
		if self.start != other.start: return False
		if self.digits != other.digits: return False
		return True

	def __add__(self, other):
		if not self.same_class(other): raise TypeError('self and other are two different classes')
		result=self.__class__(value=self.value+other.value, base=self.base, start=self.start, digits=self.digits)
		result._carry += self.carry + other.carry
		return result

	def __sub__(self, other):
		if not self.same_class(other): raise TypeError('self and other are two different classes')
		result=self.__class__(value=self.value-other.value, base=self.base, start=self.start, digits=self.digits)
		result._carry += self.carry - other.carry
		return result



