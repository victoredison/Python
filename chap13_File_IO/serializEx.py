

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of json serialization in Python'

__author__ = 'victor yu'


# When serializing Chinese characters with JSON, json.dumps() provides an ensure_ascii parameter. 

# With ensure_ascii=True: The output is ASCII-safe, meaning it can be transmitted or stored in environments that may not support non-ASCII characters.

# With ensure_ascii=False: The output retains the original non-ASCII characters, which is more readable and useful in applications that fully support Unicode (like modern web browsers and APIs).


import json

obj = dict(name='小明', age=20)

s = json.dumps(obj, ensure_ascii=True)

s1 = json.dumps(obj, ensure_ascii=False)
print('ensure_ascii set to be true')
print(s)
print('ensure_ascii set to be false')
print(s1)