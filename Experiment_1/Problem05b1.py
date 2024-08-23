# B) WAP to swap string values of two variables
# 	i) With using third variable


a = (input("Enter the first string : ")) #first string 
b = (input("Enter the second string : ")) #Second string 

#using temp as third variable to swap 
temp = a
a = b
b = temp

print(f"The first string is {a} and the second string is {b}.")