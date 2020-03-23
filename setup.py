from setuptools import setup, find_packages

def readme():
	with open('./README.md') as f:
		return f.read()

setup(
	name='slytherin',
	version='2020.3.9',

	description='Python library of useful but lonely functions and classes',
	long_description=readme(),
	long_description_content_type='text/markdown',

	url='https://github.com/idin/slytherin',
	author='Idin',
	author_email='py@idin.ca',
	license='MIT',
	packages=find_packages(exclude=("jupyter_tests", ".idea", ".git")),
	install_requires=['base32hex', 'geopy'],
	python_requires='~=3.6',
	zip_safe=False
)