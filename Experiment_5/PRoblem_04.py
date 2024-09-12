#WAP to display all the common elements of two list which 
# are inputted by the user.

n1 = input("Enter any numbers separated by spaces: ")
num1 = list(map(int, n1.split()))

n2 = input("Enter any numbers separated by spaces: ")
num2 = list(map(int, n2.split()))

common_elements = list(set(num1) & set(num2))
    
print(f"The Common elements: {common_elements}")