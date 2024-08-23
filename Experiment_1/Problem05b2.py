# B) WAP to swap string values of two variables
# 	ii) Without using third variable

a = (input("Enter the first string : ")) #first string 
b = (input("Enter the second string : ")) #Second string 

a, b = b, a

print(f"The first string is {a} and the second string is {b}.")