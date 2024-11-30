"""
Purpose: Feet to centimetres conversion

    1 foot = 12 inches
    1 inch = 2.54 centimetres

Algorithm:
----------
Step 1: Get feet values in runtime
Step 2: compute  from feet to cms
            feet to inches, then
            inches to centimeters conversion
Step 3: Display the results

"""
foot = 12 # inches
inch = 2.54 #cm

feet = int(input("Enter the feet value :"))
print("Feet :", feet)

inches = int(input("Enter the inches :"))
print("Inch :", inches)

# converting feet to inches
feet_in_inches = feet * foot

# total inches
total_inches = feet_in_inches + inches
print("Total Inches :", total_inches)

# converting to cm
value_in_cm = total_inches * inch
print("Value in Centimeters :", value_in_cm)