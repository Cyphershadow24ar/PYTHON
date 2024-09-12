# Execute an arithmetic calculator using function.

# Define the basic arithmetic functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Handle division by zero case
    if b == 0:
        return "Error: Division by zero is undefined."
    else:
        return a / b

# Main function to execute the calculator
def calculator():
    print("Welcome to the Arithmetic Calculator")
    print("Options:")
    print("1: Addition")
    print("2: Subtraction")
    print("3: Multiplication")
    print("4: Division")
    
    # Get user input
    choice = input("Choose an operation (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        # Get the numbers from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform the chosen operation
        if choice == '1':
            result = add(num1, num2)
            print(f"The result of {num1} + {num2} is {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"The result of {num1} - {num2} is {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"The result of {num1} * {num2} is {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Invalid input. Please choose a valid operation.")

# Call the calculator function to execute the program
calculator()
