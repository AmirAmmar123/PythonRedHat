#!/usr/bin/env python3
import json


"""
The json Module

The Python standard library includes a module named json that provides an API for working with JSON data.

Use the loads function to create a dictionary from a JSON formatted string.

str, bytes, or bytearray objects can be converted to a dict.

Use the dumps function to create a JSON formatted string from a dictionary.

By default, the json module performs the following object conversions:
JSON object	Python object
object 	dict
array 	list, tuple
string 	str
number (int) 	int
number (real) 	float
true 	True
false 	False
null 	None

A simple example:"""

data = '{"name": "Jill", "age": 33, "state": "MD"}'
j = json.loads(data)
print(type(j), j["state"])
print(type(j["age"]))

d = {"name": "Joe", "age": 57, "state": "PA"}
j = json.dumps(d)
print(type(j), j)