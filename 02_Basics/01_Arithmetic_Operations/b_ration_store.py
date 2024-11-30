"""
Purpose: Ration Store

--------------------------------------------------
Item    Cost        Quantity        Amount
--------------------------------------------------
Wheat   25/kg       30 kgs      25 * 30 = 750/-
Rice    12/kg       50 kgs      12 * 50 = 600/-
                            ----------------------
                                          1350/-
                            subsidy 20%   -270/-
                            ----------------------
                            BillableAmount:1000/-

Algorith
--------
Step1: Get the cost of the items into variables
Step2: Get the quanity of items into variables
Step3: Compute the selling price of each item and add 
        them
Step4: Compute the subsidy amount and subtract from the 
        selling price
Step5: Display the billable amount

"""

# cost of items
cost_of_wheat = 25
cost_of_rice = 12

# quantity of items
quantity_of_wheat = 30 # kgs
quntity_of_rice = 50 # kgs

# selling price computation
selling_price_of_wheat = cost_of_wheat * quantity_of_wheat
selling_price_of_rice = cost_of_rice * quntity_of_rice

total_selling_price = selling_price_of_wheat + selling_price_of_rice
print("Total Selling Price :", total_selling_price)

# Subsidy calculations at 20% subsidy
subsidy_amount = (total_selling_price * 20)/100 #PEMDAS
print("Subsidy amount      :", subsidy_amount)

# billable amount
billable_amount = total_selling_price - subsidy_amount
print("Billable Amount     :", billable_amount)