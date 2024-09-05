#in built functions

#eval() function is used to evaluate a string as a python expression 
# and this will be taking string as argument. and it only takes integers.
p=eval(input("Enter a number: ")) #5+5
print(p) # 10
print(eval('5+10')) #15
print('hello GOAT',p) # hello GOAT 10

name='aniket'
age='20'
print(name,age,p)

# Checking the type of each individual object
print(type(5))    # Output: <class 'int'>
print(type(2.3))  # Output: <class 'float'>
print(type('hi')) # Output: <class 'str'>

n =70.3333454532 
# the round function is used to round the integer in float to it's nearest value.
print(round(n,5))
print(round(n,4))
print(round(n,3))
print(round(n,2))
print(round(n,1))
print(round(n,0))

b =int(25.9) #type cast 
print(b) #it will return 25 not 25.9 because the variable is declared as integer.

b =max(5,10,2.5,8,9,17) # it returns the max or largest value from the list.
print(b)
b =min(5,10,2.5,8,9,17) # it returns the min or smallest value from the list.
print(b)

c =pow(3,2) # it basically  write the program as 3^2 = 9
print(c)

import math
e =25.11
print(math.ceil(e)) 
# it will return smallest integer greater than e, 26 because it will round up the value.

print(math.floor(e)) #25

print(math.fabs(e)) # it returns the absolute value , 25.11

print(math.exp(5))

print(math.log(3,3))

print(math.log(10)) # here we are passing value of x =10 and y bas base 'e'.

print(math.sqrt(4))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))
