# write a function that accepts any number of positional arguments and returns the sum of all passed arguments

def sum_of_arguments(*args):
    return sum(args)
    
user_input = input("Enter the numbers: ")

numbers = map(float, user_input.split())

sum = sum_of_arguments(*numbers)

print(f"The sum of the entered numbers is: {sum}")
