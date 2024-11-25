"""
Purpose: Identifier casing
    PEP (Python enhancement proposal) 8 - coding style
        - class names should be CamelCase
        - Identifier names should be in snake( or undo)
        
"""

# Python is case-sensitive language
animal = "DOG"
print(animal)

print(Animal)
# NameError: name 'Animal' is not defined. Did you mean: 'animal'?

ANIMAL = "PIG"
print(ANIMAL)

Animal = "Camel"
print(Animal)
# NameError: name 'Animal' is not defined. Did you mean: 'animal'?


# -----------------------------
# Variable casing
# 1. Snake casing or underscore casing
student = "Abhi"
employee_salary = 12342342.23
employee_salary = 12342342.23
cost_of_mango = 12
selling_price_of_apples = 34

output_of_thermal_sensor = 32
no_of_current_processes = 5

# 2. Camel case
Student = "Abhi"
EmployeeSalary = 12342342.23
EmployeeSalary = 12342342.23
CostOfMango = 12
SellingPriceOfApples = 34

# underscore case is called snake case because it goes up-down with every underscore added

