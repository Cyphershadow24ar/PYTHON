#[OUtput of this programme will be the value of K, l and P for each iteration 
# of function foo until the condition is true]

def foo(n, P):
    while n != 0:
        # Calculate K, update n, and update P
        K = n % 10
        n = n // 10
        P = P + K + n
        
        # Display the current values of K, n, and P
        print(f"K = {K}, n = {n}, P = {P}")
    
    # Exit when n becomes 0
    print("Exiting the function as n is 0.")
    return P

# Call the function foo with initial values
n = 3042
P = 0
final_P = foo(n, P)
print(f"Final value of P: {final_P}")
