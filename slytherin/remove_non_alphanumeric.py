import re


def remove_non_alphanumeric(s, replace_with='_', keep_underscore=True):
	s = str(s)
	if keep_underscore:
		return re.sub(r'[\W]+', replace_with, s, flags=re.UNICODE)
	else:
		return re.sub(r'[\W_]+', replace_with, s, flags=re.UNICODE)