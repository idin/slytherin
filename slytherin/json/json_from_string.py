from re import findall as re_findall
from json import loads as json_loads


def json_from_string(s):
    """
    :type s: str
    :rtype: dict
    """
    match = re_findall(r"{.+[:,].+}|\[.+[,:].+\]", s)
    return json_loads(match[0]) if match else None