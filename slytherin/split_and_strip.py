from re import sub


def split_and_strip(string, sep=','):
	if type(string) is str:
		return sub(pattern=r'\s*{0}\s*'.format(sep), repl=sep, string=string.strip()).split(sep=sep)
	else:
		return string



