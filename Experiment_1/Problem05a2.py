#5. A) WAP to swap numeric values of two variables
	# ii) Without using third variable


a = int(input("Enter the first number: ")) #first variable
b = int(input("Enter the second number: ")) #Second Variable

a = a + b
b = a - b
a = a - b

print(f"After swapping: First number = {a}, Second number = {b}.")
