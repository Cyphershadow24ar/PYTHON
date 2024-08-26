# Write a Python program to enter a 6-digit number (for example 786531) find the sum of 
# their increasing order powers (sum1=71+82+63+54+35+16) and reverse the summation of digits (sum2=11+32+53+64+85+76) . 
# find subtraction of sum2 from sum1 and print the result. 
num = (input("Enter a 6 digit number : "))
sum = 0

for i in range(len(num)):
    digit =  int(num[i])
    power = i + 1
    sum += digit ** power

print(f"The total sum is {sum}.")

rev = 0
num_int = int(num)
while num_int > 0:
    last = num_int % 10
    rev = rev * 10 + last
    num_int = num_int//10

print(f"The reverse is {rev}")
rev_str = str(rev)

sum1=0
for i in range(len(rev_str)):
    digit1 = int(rev_str[i])
    power1= i+1
    sum1 = sum + digit1 ** power1

print(f"The result is {sum1}.")
