"""

Purpose: print() function syntax and usage
    Escapes Sequence
        - character whose presence is felt, but they were not printed
        \t - tab space
        \n - new line
        \b - overwrites previous character
        
        r'' - raw string
        
    """

print("hellow world python")
print("hellow \tworld \tpython")
print("hello \tworld \npython")

print()

# To ignor the excape sequences
print("hello \tworld \\npython")
print(r"hello \tworld \\npython")

print("C:\my\newfolder")  # noqa: W605
print(r"C:\my\newfolder")
print()

# print(data, sep=' ', end = '\n')
print("hello") # default end='\n'
print("world")

print("hello", end = "__")
print("world") #default end= '\n'

print("hello", end = "\t")
print("world") #default end= '\n'

print("hello", "python", 12132, end = '\t') # default sep = ' '
print("world") # #default end= '\n'

print("hello", "python", 12132, end = "\t", sep = ";")
print("world") # default end = '\n'