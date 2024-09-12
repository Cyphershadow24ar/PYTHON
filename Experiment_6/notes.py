#there are several types of operator in python
#arithmetic operatorsc

print(9+4)
print(4-2)
print(4*2)
print(4/2)
print(5//2)
print(5%2)
print(4**2)

#relational operator or comparison operator
#always returns boolean values which is true or false

a = 2==2
print(a)
b = 2!=2
c = 2>2
d =2<5
e =1<=2
print(b)
print(c)
print(d)
print(e)

#relational operators 
f = True and True and False
print(f)
print(False or False or True)
x = 2
y = 3
z = 4

x<3 and y<z and z<x 
print(not 2==2)

#bitwise operator 
p = 4
q = 5
print(p|q)
print(p & q)
print (p^q)

crush_list = ["suhasini", "aradhana", "riya", "srishti", "twinkle"]
g ="aradhana" not in crush_list
print(g)

list1 = [1,2,3]
list2 = [2, 3, 4]
list3 = [1,2,3]
print(list1 is list2)
print(list1 is list3)

import copy 
#copy opertion in python 
# general copy shallow copy heap copy
temp1 = [1,2,["a","b"]]
temp2=[]
temp1 = temp2
print(temp2)
temp3 = temp1.copy()
temp4= copy.deepcopy(temp1)

print("loc is list1 = ", id(temp1))
print("loc is list1 = ", id(temp3))

import copy

temp4 = [1, 2, ["a", "b"]]
temp5 = copy.deepcopy(temp4)

print("Location of temp4:", id(temp4))
print("Location of temp5:", id(temp5))

print("Location of inner list in temp4:", id(temp4[2]))
print("Location of inner list in temp5:", id(temp5[2]))

def triangle():
    print('*')
    print('***')
    print('*****')
    print('*******')

def main():
    triangle()

if __name__ == '__main__':
    main()

def area():
    h = int(input("Enter the height: "))
    b = int(input("Enter the base: "))
    tri = ((1/2)*h*b)
    print(tri)

area()

def area1(b2=2):
    h1 = int(input("Enter the height: "))
    # Remove the input for b2, since it's already provided as a default argument
    tri2 = ((1/2)*h1*b2)
    print(tri2)
    
area1()

