"""
Purpose: print() function syntax and usage

"""

name = "Almighty" # string

print("name =", name)
print("Name of the student is name") # string

print("Name of the student is" + name)
print("Name of the student is " + name)

print("Name of the student is", name)
print("Name of the student is", name, sep = " ")
print("Name of the student is", name, sep = "-")
print("Name of the student is", name, sep = "")
print()

print(1, 2, 3, 4, 5, 6) # default sep
print(1, 2, 3, 4, 5, 6, sep = "")
print()

print(1, 2, 3, 4, 5, 6, sep = "~")
print(1, 2, 3, 4, 5, 6, sep = "_")
print(1, 2, 3, 4, 5, 6, sep = ":")
print()

# NOTE: Python is a dynamic typed language
name = 1232
print('Name of student is'+ name)
# TypeError: can only concatenate str (not "int") to str

# NOTE: Python is a strictly typed language

# in the interactive mode to convert into str or str to int
# >>> int('1') + 2
# 3
# >>> '1' + str(2)
# '12'


print("1 + 2         =", 1 + 2) #addition
print("'1' + '2'     =", "1" + "2") # string concatination
print()

# 1 + '2' # TypeError unsupported operand type(s) for +: 'int' and 'str'
# type converters - str(), int(), float()
print("1 + int('2') =", 1 + int("2"))
print("str(1) + '2' =", str(1) + "2")
print()

print("int('234')    =", int("234"))

# print("int('23.4')   =",  int('23.4')) # ValueError: invalid literal for 
# print("int('two')   =",  int('two'))


print("Name of Student is" + str(name))
print("Name of Student is" + " " + str(name))

