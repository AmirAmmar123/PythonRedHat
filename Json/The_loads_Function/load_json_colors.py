#!/usr/bin/env python3
import decimal
import json


"""The load Function

The load function deserializes JSON data stored in a text file.

Its functionality is similar to the loads function, because it also raises a JSONDecodeError exception on invalid data, and shares most of the optional parameters with it.

The load function also supports the fp parameter, which is the file containing JSON data.

As of Python 3.6, a binary file can also be deserialized.

The encondings supported by the load function are: UTF-8, UTF-16, or UTF-32.

The following example shows how to use the load function:"""

with open("colors.json", "r") as m:
    j = json.load(m, parse_float=decimal.Decimal)

print(type(j))
print(type(j["colors"]))
print(j["colors"][0]["name"])
value = j["colors"][0]["value"]
print(type(value), value)

print()

for color in j["colors"]:
    if "e" in color["name"]:
        print(color["name"])