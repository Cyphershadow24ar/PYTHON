# Write a program to display a/b where a and b are integers. If b = 0,
# display infinite by handling the zeroDivisionError.

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a}/{b} is: {result}")
    except ZeroDivisionError:
        print("The result of division is: infinite")

# Example usage
a = int(input("Enter the numerator (a): "))
b = int(input("Enter the denominator (b): "))
divide_numbers(a, b)
