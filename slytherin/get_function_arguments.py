def get_function_arguments(function):
	"""
	:param callable function: a function
	:rtype: list[str]
	"""
	function_arguments = list(function.__code__.co_varnames)[:function.__code__.co_argcount]
	return function_arguments
