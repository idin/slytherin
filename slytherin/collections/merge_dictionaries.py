def merge_dictionaries(x, y):
    """
    :type x: dict
    :type y: dict
    :rtype: dict
    """
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z


