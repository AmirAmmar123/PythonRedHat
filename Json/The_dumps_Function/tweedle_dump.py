#!/usr/bin/env python3
import decimal
import json
import requests


"""The dumps Function

The dumps function converts a Python object into a string representation in JSON.

The following table summarizes the available parameters for the dumps function.
obj 	The object to serialize as a JSON formatted str. This parameter is required.
skipkeys 	Ignore non-built-in data types as keys when True, raise a TypeError otherwise
ensure_ascii 	Escape all non-ASCII characters when True, convert them as-is otherwise
check_circular 	Enable or disable circular reference checks. If disabled then circular references raise an OverflowError
allow_nan 	Use the JavaScript values (NaN, Infinity, -Infinity) for the range float values (nan, inf, -inf) when True, raise a ValueError, otherwise
indent 	The indent level for JSON data. Valid values are a string, an integer , or None
separators 	A tuple in the form of (item_separator, key_separator). The default is (', ', ': ')
default 	A function to invoke for objects that cannot be serialized. The function should return a JSON encoded value or a TypeError. TypeError is raised when nothing is specified
sort_keys 	Sort the output when True.
cls 	Custom JSONEncoder subclass to use. Default is JSONEncoder
**kw 	Keyword arguments to pass to the constructor of the class specified in the cls parameter

The dump Function

The dump function is similar to the dumps function but outputs the JSON representation to a file.

The extra fp parameter controls the file to write the JSON.

As keys in key-value pairs of JSON are always str, when converting a dict to JSON, the function converts all the keys of the dict to str.

As a result, if a dict is converted to JSON and then back to a dict then the new dict may not equal the original.

The following code shows how to use the dump function:"""


seps = (',', ':')

# get the current location of the ISS
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
if response.status_code == 200:
    data = json.loads(response.content.decode())
    with open("api_data.json", "w") as r:
        json.dump(data, r, skipkeys=True,
                  separators=seps, indent=2)
else:
    print("response status:", response.status_code)

print("Done")