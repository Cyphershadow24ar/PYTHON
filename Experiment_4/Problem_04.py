# WAP to find all the prime number between 11 to 100. 
# And print their sum.
# ex input: [1 to 10]
# output: prime no.1,3,5,7 , sum =16

# start and end of the range.
start = int(input("Enter the 1st Number range: "))
end = int(input("Enter the 2nd number range: "))

sum_of_primes = 0 # Variable to store the sum of prime numbers.

print(f"Prime numbers between {start} and {end} are:")

# for loop is used here for each number in the specified range.
for num in range(start, end + 1):
    is_prime = True  # Assuming the number is prime.

    # Checking for factors from 2 to the square root of the number.
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    # If the number is prime then print and add it to the sum.
    if is_prime:
        print(num, end=", ")
        sum_of_primes += num

# Print the sum of all prime numbers.
print(f"\n Sum of prime numbers: {sum_of_primes}.")
