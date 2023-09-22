#!/usr/bin/env python3
import decimal
import json


"""The loads Function

The function raises a JSONDecodeError exception if the data being deserialized is invalid.

The loads function has several optional parameters, that you can verify in the following table:
s 	A JSON formatted str, bytes, or bytearray object to deserialize. This parameter is required.
object_hook 	A function to invoke that implements custom decoding. The return value will be used in place of dict
object_pairs_hook 	A function to invoke that implements custom decoding of ordered list of pairs. The return value will be used in place of dict. Takes priority over object_hook
parse_float 	A function to apply to each JSON float being decoded. Default is float(data)
parse_int 	A function to apply to each JSON int being decoded. Default is int(data)
parse_constant 	Can be '-Infinity', 'Infinity', 'NaN' and is used to raise an exception when decoding invalid JSON numbers
cls 	A custom JSONDecoder subclass to be used. Default is JSONDecoder
**kw 	Keyword arguments to be passed to the constructor of the class specified in the cls parameter

The following code shows how to use the loads function:"""

data = '{"x": 0.1, "y": 0.2}'
j = json.loads(data)
j_x = j["x"]
j_y = j["y"]
print(type(j), type(j_x), j_x, sep=", ")
print(j_x + j_y)

j = json.loads(data, parse_float=decimal.Decimal)
j_x = j["x"]
j_y = j["y"]
print(type(j), type(j_x), j_x, sep=", ")
print(j_x + j_y)

data = '{"name": "Jill", "age": 33, "state": "MD"}'
j = json.loads(data, parse_int=str)
print(type(j["age"]), j["age"], sep=", ")