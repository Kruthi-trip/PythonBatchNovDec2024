#!/usr/bin/python3
"""
Purpose: working with comment operator
    - Once # is encountered, complete line from that position is ignored
    - PEP 8 recommends one white space after # operator
    - Comments
        - single line comment  #
        - Multi-line comment - python doesnt support


Question: why python doesnt have multi-line comment operator
Answer: Python is a interpretor based language, means each line executes one after the other

Python code -> line by line -> c code -> assembly -> machine

print('Hello World1')
"""

print('Hello World2')
# print ('Hello World3')

# any operator within quotes will be treated as a string
print("Hello #World4")
print("Hello", "World5", sep="#")

print("Hello world6") # jgdvcjgvejcvjhe
print("Hello world7") # this is about the world

'''
used to handle multi-line strings
or
incase where multiiple single and double quotes are used
'''

"""
used for docstrings

print('Hello world8)
"""