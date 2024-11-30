"""
Purpose: Grocery Store

    Item       cost
    ------------------------
    rice        10/kg
    wheat       34/kg

Algorithm
---------
Step 1: Get the cost of items into variables
Step 2: Get the quantity of items from the user(in run time)

NOTE: input()
        -> to get value in run-time
        -> will give any input as string only
"""

# Cost of items
cost_of_rice = 10 # per kg
cost_of_wheat = 34 # per kg

# quantity of items
quantity_of_rice = input("Enter Qty. of Rice : ")
quantity_of_rice = float(quantity_of_rice)
print("Quantity of Rice :", quantity_of_rice)


quantity_of_wheat = float(input("Enter Qty. of Wheat : "))
print("Quantity of Wheat :", quantity_of_wheat)


# selling price computation
selling_price_of_rice = cost_of_rice * quantity_of_rice
print("Selling Price of Rice :", selling_price_of_rice)

selling_price_of_wheat = cost_of_wheat * quantity_of_wheat
print("Selling Price of Wheat :", selling_price_of_wheat)

total_selling_price = selling_price_of_rice + selling_price_of_wheat
print("Total Selling Price :", total_selling_price)