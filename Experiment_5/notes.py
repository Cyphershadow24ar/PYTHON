# i=1 # Initialize i
# while i<=10:
#     print(i)  #NOTE: print 1 to 10
#     i = i+1

# j=1
# while j<=100:
#     print(j) #NOTE: print 1 to 100
#     j= j+1

# k=100
# while k>=1:
#     print(k) # NOTE: print 100 to 1
#     k = k-1

# z=50
# while z<=100:
#     print(z) # NOTE: print 50 to 100 and even only
#     z = z+2

# y = int(input("Enter a number: "))
# x = 1  # Initialize i
# while x <= 10:
#     product = y * x
#     print(f"{y} x {x} = {product}")  #NOTE: multiplication table
#     x = x + 1

#NOTE: Create a list and take input from user and check wether that element is present in list or not !?
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = int(input("Enter the value: "))

# found = False  # Flag to indicate if x is found and also is true or false 
# for item in list1:  # Iterate through each item in list1
#     if item == x:
#         found = True
#         break

# if found:
#     print("Yes")
# else:
#     print("No")


#NOTE: FOR LOOP
# crush_list = ["lili","jhili","mili","rupali","sili"]
# for item in crush_list:
#     print(item)

# num = [1,2,3,4,5]
# num.reverse()
# for i in num:
#     #print(i)
#     print(i)

# num1 = [1,2,3,4,5]
# i=4
# while i>=0:
#     print(num1[i])
#     i=i-1

# def welcomeAboard(name):
#     name = (input("Enter the name: "))
#     print (f"Welcome {name}")

# welcomeAboard()

# list1 =[3,4,5,6,7]
# n=int(input("Enter the value: "))
# for i in list1==n:
#     j=1
#     while j<=10:
#         print(i,"x",j,"=",i*j)
#         j=j+1

# crush_list=["riya","piya","giya","miya","siya"]
# for i in range(5):
#     print("gf",i+1,":",crush_list[i])
# NOTE: output of the above code.
# gf 1 : riya
# gf 2 : piya
# gf 3 : giya
# gf 4 : miya
# gf 5 : siya

n = int(input("Enter the number: "))

if n <= 1:
    print(f"{n} is not a prime number.")
else:
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")

