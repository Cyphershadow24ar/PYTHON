n=(input("Enter any numbers :"))
num = list(map(int, n.split()))

even_num= []
odd_num = []

for item in num:
    if item%2 == 0:
        even_num.append(item)
    elif item%2 !=0:
        odd_num.append(item)
        
print(f"The Even numbers are {even_num}.")        
print(f"The Odd numbers are {odd_num}.")        