# WAP to enter two number from user input 
# and find their LCM and HCF

a = int(input("Enter the 1st NO.: "))
b = int(input("Enter the 2nd NO.: "))

#here take num1 , 2 as a and b.
num1 = a
num2 = b

#using while loop for continue finding the remainder until the remainder is 0.
while num2 != 0:
    remainder = num1 % num2
    num1 = num2
    num2 = remainder

# The last non-zero value of num1 is the HCF.
hcf = num1

# TO find lcm we are using the formula.
lcm = (a*b)//hcf

print(f"HCF of {a} and {b} is {hcf}.")
print(f"LCM of {a} and {b} is {lcm}.")