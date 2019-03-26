import inspect

def serialize_arguments(exclude=None):
    """
    when put inside a function, it produces a dictionary of all arguments passed into the function
    :param list[str] or NoneType exclude: arguments to exclude
    :rtype: list[tuple]
    """
    exclude = exclude or []
    frame = inspect.currentframe().f_back
    args, _, _, values = inspect.getargvalues(frame)
    result = []
    for arg in args:
        if arg not in exclude:
            result.append((arg, values[arg]))
    return result