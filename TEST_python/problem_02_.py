# Write a python program to evaluate the function cos(x) as defined by the infinite series expansion. 
# cos(x) = 1-x^2 /2! + X^4/4! - x^6/6! + ...
# The acceptable error for computation is 10^6.

import math

theta = float(input("Enter the angle in degrees: "))

x = math.radians(theta)

cos_x = 1  
term = 1   
n = 1       
tolerance = 1e-6  

while abs(term) > tolerance:
    term = (-1) ** n * (x ** (2 * n)) / math.factorial(2 * n)
    cos_x += term
    n += 1

# Output the result
print(f"The computed value of cos({theta}°) is approximately {cos_x}")
print(f"The actual value of cos({theta}°) from math module is {math.cos(x)}")

