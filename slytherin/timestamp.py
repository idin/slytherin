from datetime import datetime
import os
import errno

class TimeStamp:
	def __init__(self, date = datetime.today(), prefix = '', suffix = '', echo = True):
		self._date = date
		self._prefix = prefix
		self._suffix = suffix
		self._dir = None
		self._echo = echo

	def stamp(self, date=datetime.today(), format = "%Y-%m%d-%H%M"):
		the_stamp = self._prefix + self._date.strftime(format) + self._suffix
		if self._echo:
			print('stamp:', the_stamp)
		return the_stamp

	def make_dir(self):
		dir_name = self.stamp()

		try:
			os.makedirs(dir_name)
		except OSError as e:
			if e.errno != errno.EEXIST:
				raise
		if self._echo:
			print('make dir:', dir_name)
		self._dir = dir_name

	def get_path(self, file):
		the_path = self._dir + '/' + file
		if self._echo:
			print('file path:', the_path)
		return the_path
