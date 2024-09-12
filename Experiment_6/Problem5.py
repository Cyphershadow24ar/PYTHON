# Write a Programme in python to check a user inputted string is 
# palindrome or not by using function.

# Function to check if a string is a palindrome
def is_palindrome(input_string):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = input_string.replace(" ", "").lower()
    
    # Check if the string is the same when reversed
    if cleaned_string == cleaned_string[::-1]:
        return True
    else:
        return False

# Main function to get user input and call the palindrome function
def check_palindrome():
    # Get the input from the user
    user_string = input("Enter a string: ")
    
    # Check if the input string is a palindrome
    if is_palindrome(user_string):
        print(f"'{user_string}' is a palindrome.")
    else:
        print(f"'{user_string}' is not a palindrome.")

# Call the main function to run the program
check_palindrome()
