# Write a python programme to do the addition and multiplication of number
# inputted from user in the form of tuple(use function)
# [Collect the value of tuples from user then convert it into list and run
# function to do the addition and multiplication.]

# Function to perform addition of numbers in a list
def add_numbers(numbers_list):
    return sum(numbers_list)

# Function to perform multiplication of numbers in a list
def multiply_numbers(numbers_list):
    result = 1
    for num in numbers_list:
        result *= num
    return result

# Main function to get input, convert tuple to list, and call other functions
def process_tuple():
    # Collect tuple input from user as a string, then evaluate it as a tuple
    user_input = input("Enter numbers separated by commas in a tuple format (e.g., 1, 2, 3): ")
    
    # Convert the input string to a tuple using eval (Note: Use eval cautiously)
    numbers_tuple = eval(f"({user_input},)")
    
    # Convert the tuple to a list
    numbers_list = list(numbers_tuple)
    
    # Perform addition and multiplication using the functions
    total_sum = add_numbers(numbers_list)
    total_product = multiply_numbers(numbers_list)
    
    # Display the results
    print(f"List of numbers: {numbers_list}")
    print(f"Sum of numbers: {total_sum}")
    print(f"Product of numbers: {total_product}")

# Call the main function to run the program
process_tuple()
