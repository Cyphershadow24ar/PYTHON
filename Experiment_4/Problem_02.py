#WAP to input a number through user and check 
# whether the number is a. Armstrong number
# b. perfect number
# c. adam number
# d. Palindrome Number 

# Input the number from the user
n = int(input("Enter the number: "))

# Check if the number is an Armstrong number

num_str = str(n)
num_digits = len(num_str)
sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
armstrong = (sum_of_powers == n)

# Check if the number is a perfect number

sum_of_divisors = sum(i for i in range(1, n) if n % i == 0)
perfect = (sum_of_divisors == n)

# Check if the number is a palindrome

num_str_reversed = num_str[::-1]
palindrome = (num_str == num_str_reversed)

# Check if the number is an Adam number

reversed_n = int(num_str[::-1])   # Reverse the number
n_squared = n ** 2   # Square both numbers
reversed_n_squared = reversed_n ** 2

# Check if both squares are palindromes
n_squared_str = str(n_squared)

reversed_n_squared_str = str(reversed_n_squared)

is_n_squared_palindrome = (n_squared_str == n_squared_str[::-1])

reversed_n_squared_palindrome = (reversed_n_squared_str == reversed_n_squared_str[::-1])

adam = is_n_squared_palindrome and reversed_n_squared_palindrome

# Print results with modified statements
print(f"Number {n} is an Armstrong number: {'Yes' if armstrong else 'No'}")
print(f"Number {n} is a perfect number: {'Yes' if perfect else 'No'}")
print(f"Number {n} is an Adam number: {'Yes' if adam else 'No'}")
print(f"Number {n} is a palindrome number: {'Yes' if palindrome else 'No'}")
