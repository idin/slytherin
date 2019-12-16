class Series:
	def __init__(self, start, end, step):
		self.start = start
		self.end = end
		self.step = step

	def generate(self):
		num = self.start
		while num <= self.end:
			yield num
			num += self.step

	def __getstate__(self):
		return (self.start, self.end, self.step)

	def __setstate__(self, state):
		self.start, self.end, self.step = state

	def __hashkey__(self):
		return (self.__class__.__name__, self.__getstate__())

	@property
	def list(self):
		return list(self.generate())