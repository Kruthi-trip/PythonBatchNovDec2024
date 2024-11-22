"""
Purpose: Inmportance of indentation

"""

print("Hello World 1")
#  print("Hello World 2") # IndentationError: unexpected indent(not needed but given)
print("Hello World 3")


# block code - if, else, elif, for, while, def, class, ...
# if 12 > 3:
# print('12 is greater than 3')
#IndentationError: expected an indented block after 'if' statement on line 12

if 12 > 3:
    print('12 is greater than 3')


if 12 > 34:
    print("greater")
else:
    print("It is lesser")



if 1< 2:
    print("Case 1")
elif 2 > 1:
    print("Case 2")
else:
    print("Case 3")


if 1 < 2:
    if 2 < 3:
        if 3 < 4:
            if 4 < 5:
                print("LESSER")
            else:
                print("Something")
        else:
            print("Something")
    else:
        print("Something")


for i in range(9):
    print(i)


i = 0
while i < 10:
    print(i)
    i += 1


i = 0
while i < 10:
    j = 0
    while j < 10:
        print(i, "*", j, "=", i * j)
        j += 1
    print()
    i += 1


def my_func():
    return "hello world"

class MyClass:
    def __init__(self):
        pass


# tabs vs white space
# PEP 8 (python enhancement proposal) - code style guide
# prefer white spaces, to tabs; four white spaces