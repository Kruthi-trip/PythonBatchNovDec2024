"""
Purpose: Saving Bank

    Initial Balance 0

Algorithm
----------
Step 1: Create an variable 'balance' with initial value 0
Step 2: Initial Despoit of min balance 1500
Step 3: Salary credited of 3300
Step 4: Online Purchase of 33.33
Step 5: House Rent paid of 1500
Step 6: Display Balance

"""

# creating variables 
balance = 0
minimum_balance = 1500
salary = 3300
house_rent = 1500
online_purchase = 33.33

# Initial deposit to the account
updatedBalance = balance + minimum_balance

# salary credited
updatedBalance = updatedBalance + salary

# online purchase(debited)
updatedBalance = updatedBalance - online_purchase

# paid house rent
updatedBalance = updatedBalance - house_rent

# displaying current balance
print("Current Balance :", updatedBalance)