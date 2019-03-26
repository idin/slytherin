def textfile_to_string(path, replace_return=None):
	with open(path, 'r') as myfile:
		data = myfile.read()

	if replace_return is not None:
		data = data.replace('\n', replace_return)
	return data


