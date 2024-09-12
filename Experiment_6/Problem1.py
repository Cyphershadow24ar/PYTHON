# Write a programme in python using function to execute the given tree by displaying 
# the values of statements present in the level 1 and whenever the value of n is equals 
# to 0 the function will get exit and return 0 (call the function foo with the value 
# (3042,0) and foo will call itself by the updated value of n and p).

def foo(p, n):
    # Level 1: Display current values of p and n
    print(f"Level 1: p = {p}, n = {n}")
    
    # Base case: exit if n is 0
    if n == 0:
        print("Exiting function as n is 0.")
        return 0

    # Update p and n (example logic: subtract 1 from p and n)
    new_p = p - 1
    new_n = n - 1

    # Recursive call with updated values
    return foo(new_p, new_n)

# Call the function with the values (3042, 0)
foo(3042, 0)
