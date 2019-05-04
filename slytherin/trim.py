from math import ceil, floor


def trim(string, max_length=None, cut_from='middle'):
	"""
	:param str string: string to be shortened
	:param int or NoneType max_length: if None, the string will only be stripped of leading and trailing white spaces
	:param str cut_from: example: 'what a wonderful world!'    end --> 'what ...', middle --> 'wh ... ld', start --> ' ... world'
	:rtype: str
	"""
	string = str(string).strip()
	if max_length is None:
		return string

	max_length = int(max_length)
	cut_from = cut_from.lower()
	if len(string) > max_length:
		if cut_from == 'end':
			return string[:max_length - 4] + ' ...'
		elif cut_from == 'start':
			return '... ' + string[len(string) - max_length + 4:]
		elif cut_from == 'middle':
			length_allowed = max_length - 5
			left_side = ceil(length_allowed / 2)
			right_side = floor(length_allowed / 2)
			return string[:left_side] + ' ... ' + string[len(string) - right_side:]
	else:
		return string