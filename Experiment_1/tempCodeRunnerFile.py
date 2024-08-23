# WAP to calculate the following equation by inputting the value of x, y and n in the range [2 to 8].

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
n = int(input("Enter the value of n: "))

Equation = (((x**3 + x**3) / (y/4 + y/3 + y**8))**2 * n) * ((y**6 + y**2) / x**9)

print(f"The solution of this equation is {Equation}.")