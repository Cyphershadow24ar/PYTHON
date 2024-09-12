#WAP to count positive number, negative number and zeros
# in a list.

n=(input("Enter any numbers: "))
num =(list(map(int, n.split())))

positive_num=[]
negative_num=[]
zero_num=[]

for i in num:
    if i>0:
        positive_num.append(i)
    elif i<0:
        negative_num.append(i)
    elif i==0:
        zero_num.append(i)

print(f"The Positive numbers: {positive_num}")
print(f"The Negative numbers: {negative_num}")
print(f"The zero numbers: {zero_num}")
