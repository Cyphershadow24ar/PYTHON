#Write a Python code to design an arithmetic calculator(+,-,*,/,%,<<,>>) with inputting 2 numbers.

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Input the operation
operation = input("Enter the operation (+, -, *, /, %, <<, >>): ")

# Switch-case like structure using a dictionary
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
elif operation == '%':
    result = num1 % num2
elif operation == '<<':
    result = num1 << num2
elif operation == '>>':
    result = num1 >> num2
else:
    result = "Invalid operation"

# Print the result
print(f"The result of {num1} {operation} {num2} is: {result}")
