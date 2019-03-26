from urllib.request import urlopen
from .json_from_string import json_from_string


def json_from_url(url):
	"""
	:type url: str
	:rtype: dict
	"""
	with urlopen(url=url) as url:
		data = json_from_string(url.read().decode())
	return data