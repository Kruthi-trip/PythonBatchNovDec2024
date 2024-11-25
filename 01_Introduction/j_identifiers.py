"""
Purpose: Identifiers in python

    Variable
        1. Keyword --> words which have some meaning in that language
        2. Identifiers --> words which are defined by user(developers)
        

    Modules are like libraries
"""

# loading a module
import keyword

print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async',
# 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
# 'else', 'except', 'finally', 'for', 'from', 'global', 'if',
# 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
# 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

print(True)

# print(true)
# NameError: name 'true' is not defined. Did you mean: 'True'?

my_value = "something"
print(my_value) # Identifier

# True = "something"
# SyntaxError: cannot assign to True

print(keyword.iskeyword("True"))        # True
print(keyword.iskeyword("true"))        # False
print(keyword.iskeyword("my_value"))    # False


# ----------------------------------------------------------------
# Identifiers - User-defined Variables
#     - Naming Convention
#         1. Keywords should not be used as identifiers
#         2. first character: a-z, A-Z, _
#         3. remaining chars: a-z, A-Z, _, 0-9

# ----Rule 1
# True = 123 # SyntaxError: cannot assign to True
# None = 'Nothing' # SyntaxError: cannot assign to None

# PEP 8 - Dont create identifiers which are similar to the keywords
true = 123
none = "Nothing"

true_value = 123
none_result = "Nothing"

# ---- Rule 2 & 3
Name = "Kruthi"
name_of_student = "Kruthi"
first_name = "Kruthi"
student_1 = "Kruthi"
class_02_a = "Python comment operators"
first____child = "Kruthi"

#  PEP 8 recommendations to use capitals for constants
PI = 3.1416
DOZEN = 12

# # $name = "Kruthi"
# name-of-student = "Kruthi"
# SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
# name of student = "Kruthi"
# IndentationError: unexpected indent

# 1st_name = "Kruthi"
# # cannot have numbers as the first character

_2nd_student = "Someone"

_job = "software development"
__role = "Product Support"
___Salary = 123123123123123


# OOP -> name mangling
# variable   -> Public variable
# _variable  -> Protected Variable
# __variable -> Private variable

# __Variable__ -> Built-in functions
# Ex: __file__, __name__, __doc__, __dict__, __init__


# print("__name__=", __name__) #__main__
# print("__file__=", __file__)
# # __name__= __main__
# __file__= /workspaces/PythonBatchNovDec2024/01_Introduction/j_identifiers.py

# print("__Lohit__=", __Lohit__)
# NameError: name '__Lohit__' is not defined

