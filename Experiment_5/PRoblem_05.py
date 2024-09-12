# WAP to find the average of 
# maximum and minimum element of a list 

n1 = input("Enter any numbers separated by spaces: ")
num1 = list(map(int, n1.split()))

maxL1= max(num1)
minL1= min(num1)

average = ((maxL1+ minL1)/2)

print(f"The Maximum number: {maxL1}")
print(f"The Minimum number: {minL1}")
print(f"The Average of Maximum and Minimum : {average}")