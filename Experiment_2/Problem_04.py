# Write a Python program to input 2 strings and insert side-by-side one character from string 2 in string1. 
# (For Ex: String1="Amar", String1="Peter", result= "APmeatrr")

name1= (input("Enter the first name: "))
name2= (input("Enter the Second name: "))

len1= len(name1)
len2= len(name2)
result =""

for i in range(max(len1,len2)):
    if i<len1:
        result = result + name1[i]
    if i<len2:
        result = result + name2[i]

print(f"The result of the given input is {result}.")