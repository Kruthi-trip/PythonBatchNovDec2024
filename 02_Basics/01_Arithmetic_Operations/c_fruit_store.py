"""
Purpose: Fruit Store

    Items   price       qty                         amount
    -----------------------------------------------------------
    Apples   12/piece   5 dozens = 5 * 12 = 60      12 * 60
    Mangos   34/piece   3 dozens = 3 * 12 = 36      34 * 36
                                                ---------------
                                                      1944   /-
                                discount     -2 %     - 38.88/-
                                                ---------------
                                                      1905.12/-
                                GST         +12.5 %   +238.14/-
                                                ---------------
                                                      2143.26/-
           
Algorithm
----------
Step 0 : declare the constants
Step 1:  Get the cost of fruits into variables
Step 2:  Get the quantity of fruits into variables.
         Compute the end quantity, by substituting dozen value.
Step 3:  Compute the selling price to each item,
         and add them
Step 4:  Compute the discount amount and subtract
         from the selling price, to create payable amount
Step 5:  Calculate GST amount and Add to payable amount,
         to create billable amount
"""

# cost of the fruits
cost_of_apple = 12
cost_of_mango = 34

# assigning variables
DOZEN = 12
DISCOUNT = 2
GST = 12.5

# quantity of fruits
quantity_of_apple = DOZEN * 5
quantity_of_mango = DOZEN * 3

# selling price of fruits
selling_price_of_apple = cost_of_apple * quantity_of_apple
selling_price_of_mango = cost_of_mango * quantity_of_mango

selling_price = selling_price_of_apple + selling_price_of_mango
print("Selling Price                :", selling_price)

total_discount = (selling_price * DISCOUNT)/100
print("Total Discount               :", total_discount)

selling_price_after_dicount = selling_price - total_discount
print("Selling Price after Discount :", selling_price_after_dicount)

total_gst = (selling_price_after_dicount * GST)/100
print("Total GST amount             :", total_gst)

billable_amount = selling_price_after_dicount + total_gst
# print("Billable Amount              :", billable_amount)

# round(num, no_of_digits) - function
print("Billable Amount              :", round(billable_amount, 2))