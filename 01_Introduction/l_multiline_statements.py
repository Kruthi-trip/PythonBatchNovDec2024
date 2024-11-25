r"""
Purpose: Working with Multi-line statements

    Python is a interpreter-based language
        - Each line executes seperate
        - \ -> Line continuation operator
        - will join more than one line to a single 
        
        
    Brace
        () Paranthesis
        [] square braces
        {} flower braces
        
        
    PEP 8:
        a) Lines should be 79 characters in length and less
        b) Continuations of long expressions onto additional
            indented by four extra spaces from their normal
            
            
"""

sum_of_values = 123 + 23 - 123 * 2 / 12
print(sum_of_values)


sum_of_values = 123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12
print(sum_of_values)

# if we put the same in two lines it will give an error thinking they are two different lines.
# but to still use two lines and execute the code without an error we can use '\'.
# for the same thing we cannot use a comment in between

sum_of_values = 123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12 + 123 + \
23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12
print(sum_of_values)


# braces alongside line continuation operator
sum_of_values = (123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12 + 123 + \
23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + \
23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12)
print(sum_of_values)


# braces alone
sum_of_values = (123 + 23 - 123 * 2 / 12 + 123 + 23 - 123 * 2 / 12 + 123 + 
23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12 / 123 + 23 - 123 * 2 / 12 - 123 + 
23 - 123 * 2 / 12 - 123 + 23 - 123 * 2 / 12)
print(sum_of_values)