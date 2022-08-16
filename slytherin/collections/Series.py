class Series:
	def __init__(self, start, end, step=None, count=None, include_start=True, include_end=True):
		self._start = start
		self._end = end

		if count is None and step is None:
			raise ValueError('either count should be given or step!')
		elif count is not None and step is not None:
			raise ValueError('only one of step and count should be given!')
		elif step is not None:
			if start <= end:
				step = abs(step)
			else:
				step = -abs(step)

		if not include_start and not include_end:
			raise ValueError('either start or end should be included!')

		self._step = step
		self._count = count
		self._include_start = include_start
		self._include_end = include_end

	def generate(self):
		if self._include_start and self._include_end:
			if self._count is None:
				num = self._start
				while num <= self._end:
					yield num
					num += self._step
			else:
				step = (self._end - self._start) / (self._count - 1)
				for i in range(self._count - 1):
					yield self._start + i * step
				yield self._end

		elif self._include_start:
			if self._count is None:
				num = self._start
				while num < self._end:
					yield num
					num += self._step
			else:
				step = (self._end - self._start) / self._count
				for i in range(self._count):
					yield self._start + i * step
		elif self._include_end:
			if self._count is None:
				count = (self._end - self._start) // self._step
				start = self._end - count * self._step
				if start != self._start:
					for i in range(count, -1, -1):
						yield self._end - i * self._step
				else:
					for i in range(count - 1, -1, -1):
						yield self._end - i * self._step
			else:
				step = (self._end - self._start) / self._count
				for i in range(1, self._count):
					yield self._start + step * i
				yield self._end
		else:
			raise ValueError('either start or end should be included!')

	def __getstate__(self):
		return self._start, self._end, self._step, self._count, self._include_start, self._include_end

	def __setstate__(self, state):
		self._start, self._end, self._step, self._count, self._include_start, self._include_end = state

	def __hashkey__(self):
		return self.__class__.__name__, self.__getstate__()

	@property
	def list(self):
		return list(self.generate())
