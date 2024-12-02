##### Assignment: 
    # test if a given sentence is palindrome or not
    # HINT: ignore the whitespace and check

test_string = "todayisgoodday"

reverse_string = test_string[::-1]


print("test_string == reverse_string:", test_string == reverse_string)


if test_string == reverse_string:
    print(test_string, "is Palindrome")
else:
    print(test_string, "is NOT a Palindrome")