"""
Purpose: multiple statements in same line
    , logic seperator
    ; statement completion operator
"""

print("Hello" "world")
print("Hello", "world")

print("Hello", 21312)
# print("Hello" 21312)
# yntaxError: invalid syntax. Perhaps you forgot a comma?

print("Hello", 21312, 213,123 + 123 -3)
print()

# comma gives a white space between two things we are trying to join
# this is only when trying to add anyting other than numbers

# Semicolon operator

# Method 1
num1 = 100
num2 = 200
sum_of_numbers = num1 + num2
print("Sum Of Numbers =", sum_of_numbers)


# Method 2 using ; operator
num1 = 100; num2 = 200; sum_of_numbers = num1 + num2; print("Sum Of Numbers =", sum_of_numbers)


# Conclusion
# 1. ; is optional. will not change anything.
# 2. ; is important if we need to write more than one statement in same line
# 3. Unnecessarily placing a semicolan at the end of statement will increase

"""
python -c "print('hello world')"

python -c "num1 -123; num2 = 300; sum_of_numbers = num1 + num2; print("Sum Of Numbers =", sum_of_numbers)


language
    - scripting language Ex: batch, shell,...
    - general purpose programming language Ex:  C, C++. JAVA,
    
    
python is both scripting and general purpose programming language


.bat
    cd directory1
    cd subdirectory2
    ping google.com > result.txt
    
"""