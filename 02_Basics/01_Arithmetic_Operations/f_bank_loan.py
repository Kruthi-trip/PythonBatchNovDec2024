"""
Purpose: Bank Loan

    Simple Interest : A = P (1 + rt)

                        A	=	final amount
                        P	=	initial principal balance
                        r	=	annual interest rate
                        t	=	time (in years)

Ref :https://www.calculatorsoup.com/calculators/financial/simple-interest-plus-principal-calculator.php




# compount interest
REF: https://www.calculatorsoup.com/calculators/financial/compound-interest-calculator.php


"""

# assigning user input variables
initial_principal = float(input("Enter the initial Principle amount: "))
P = initial_principal
print("P = ", P)

annual_interest_rate = float(input("Enter the annual interest rate : "))
r = annual_interest_rate / 100
print("r =", r)

loan_duration = int(input("Enter the loan duration(yrs): "))
t = loan_duration
print("t =", t)

# calculating the simple interest
# A = P (1 + rt)

final_amount = P *(1 + (r * t))
A = final_amount
print("Final Amount(A): ", final_amount)


