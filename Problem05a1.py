"""A) WAP to swap numeric values of two variables
	i) With using third variable"""
	

a = int(input("Enter the first number: ")) #first variable
b = int(input("Enter the second number: ")) #Second Variable

# Using a third variable as temp
temp = a
a = b
b = temp

print(f"After swapping: First number = {a}, Second number = {b}.")
