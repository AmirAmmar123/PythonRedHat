#!/usr/bin/env python3

first = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
second = ["day", "day", "sday", "nesday", "rsday", "day", "urday"]
[ print("".join(x)) for x in zip(first ,second) ]