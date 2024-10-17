#WAP in python to add two numbers using module.

import mymath

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2st number: "))

sum = mymath.add_numbers(num1,num2)
print(f"The Sum is: {sum}")