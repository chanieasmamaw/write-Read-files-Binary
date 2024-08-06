# Task 1
# Improve Code Styling: Ensure proper indentation and spacing.
# Add Documentation: Write a docstring for the function.
# Use Constants: Define π (pi) as a constant.

# PI is as constant
PI = 3.14159
# Calculating the area of circle and it returns as float
def calc_area(radius:float)->float:
   
    return PI * radius * radius
#Define the radius
radius = 5
area = calc_area(radius)
print("Area:", area)

# Task 2
# Rename Variables: Use more descriptive names.
# Improve Readability: Add type hints and a docstring.
# Use Constants: If applicable, identify any magic numbers and define them as constants.
#calculating the sum of list integers
def calculate_sum(list_num):
    total = 0
    for i in list_num:
        total += i
    return total
#define the list of numbers
nums = [1, 2, 3, 4, 5]
print(f"Sum:", calculate_sum(nums))

# Task 3
# Use Constants: Define the conversion factors as constants.
# Add Documentation: Write a docstring for the function.
# Improve Naming: Use descriptive variable names and type hints.
#Tempreture conversion factors as constant convert from celsius to farahanight
def convert_temp(celsius:float)->float:
    return celsius * 9/5 + 32

temp_celsius = 30
#conversion from celsius to fahrenheit
temp_fahrenheit = convert_temp(temp_celsius)
#Print in Fahrenheit
print(f"Temperature in Fahrenheit:", temp_fahrenheit)
