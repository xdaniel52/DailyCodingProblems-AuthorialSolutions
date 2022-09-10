# -*- coding: utf-8 -*-
"""
This problem was asked by Dropbox.

What does the below code snippet print out? 
How can we fix the anonymous functions to behave as we'd expect?

functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
"""

functions = []
for i in range(10):
    functions.append(lambda j=i: j)

for f in functions:
    print(f())