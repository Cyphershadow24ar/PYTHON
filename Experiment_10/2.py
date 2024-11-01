try:
    # Attempting a division by zero
    x = 10 / 0
except ZeroDivisionError:
    print("Caught ZeroDivisionError: Cannot divide by zero")

try:
    # Attempting to access an index that is out of bounds
    list_example = [1, 2, 3]
    print(list_example[5])
except IndexError:
    print("Caught IndexError: List index out of range")

try:
    # Attempting to convert a string to an integer
    num = int("abc")
except ValueError:
    print("Caught ValueError: Cannot convert string to integer")