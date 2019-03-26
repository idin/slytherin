# Slytherin
Slytherin is a collection of useful but lonely functions and classes 
that don't belong to other libraries.

## Installation
```bash
pip install slytherin
```

## Usage

### get_size(obj)
The *get_size()* method calculates the memory footprint of a Python object recursively. 

The *exclude_objects* argument is a list of objects and is optional with the default value
of None. 
Any object in the *exclude_objects* list will be excluded from the recursive search. 
It can be used to avoid double counting the size when objects point to each other. 

```python
from slytherin import get_size
get_size(obj=[1,2,3], exclude_objects=None)

import pandas as pd
get_size(obj=pd.DataFrame({'id': range(1000), 'name':['Godric', 'Helga', 'Rowena', 'Salazar']*250}))
```

### colour(text, text_colour, style, background_colour)
The *colour()* method can be used to add colour to printing text.

The colour are integers from 0 to 7:
* black: 0
* red: 1
* green: 2
* yellow: 3
* blue: 4
* purple: 5
* cyan: 6
* white: 7

The *style* argument is an integer between 0 and 5:
* normal: 0
* bold: 1
* underline: 2
* negative1: 3
* negative2: 5

```python
from slytherin import colour
print(colour(text='Hello world!', text_colour=4))
```