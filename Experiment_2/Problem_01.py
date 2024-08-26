#Write a Python program to perform addition and subtraction of two complex number to be inputted from standard keyboard. 

C1=(complex(input("Enter the first Complex Number: ")))
C2=(complex(input("Enter the Second Complex Number: ")))

addition = C1 + C2
subtraction = C1 - C2

print(f"The addition of {C1} and {C2} = {addition}")
print(f"The subtraction between {C1} and {C2} = {subtraction}")