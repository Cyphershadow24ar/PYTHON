mili_shayari = '''Jab se mile ho tum, dil ko ek sukoon mila hai,
                Tumse baat karne ka mili mazaa kuch aur hi hai,
                mera har khushi mein tumhara hi junoon mila hai.'''


#here the .replace function is used to replace the specific word in the string.
riya_shayari = mili_shayari.replace("mili","riya")
print(riya_shayari) 

# .upper changes the alphbelts from lower case to UPPER CASE.
print(riya_shayari.upper())

# .lower changes the alphbelts from UPPER CASE to lower case.
print(riya_shayari.lower())

temp ="we Guys wab bhut way accha ho."
print(temp.capitalize()) # only the first letter of the sentence get's capital.

print(temp.title()) # Each and every word's first letter get's capital.

print(temp.index('u')) #it returns the index value of the letter you want.

print(temp.index('a',18))

print(temp.index("w",temp.index("w")+1)) 
# by using this type of method we find the same the type of alphabet at a different position or at the next position.

print(temp.index("w",temp.index("w")+1)+1) 

print(temp.rindex("w")) 

print(temp.split("u"))

print(temp.find("y"))

#to add a word in the list at last position so for this we use .append function
name= ["ani","bunny","honey","bannii"]
name.append("ket")
print(name)

name.insert(0,"my")
print(name)

name2 = ["my", "name", "is", "ChatGPT"]

# Removing "my" from the list
name2.remove("my")  # This will remove the first occurrence of "my" from the list
print(name)

# Popping the first element (if you want to pop by value, you should use remove instead)
popped_value = name2.pop(0)  # This will remove and return the element at index 0
print(popped_value)
print(name2)

# Clearing the entire list
name.clear()  # This will remove all elements from the list
print(name2)

#this sort function is used here for sorting and it will sort it in ascending  order
list1 =[2,4,5,7,23,5,0]
list1.sort()
print(list1)
# to sort it in the descending we use 'reverse =true'.
list1.sort(reverse=True)
print(list1)

list2=['riya','priya','sia','mia', 'zahar']
list2.sort()
print(list2)

new= list2.copy()
print(new)

std = {'lol': 20, 'raj': 21, 'why': 40}

# Attempting to get the value for the key "lol"
print(std.get("lol"))  # Output: None, because "lol" is not a key in the dictionary

# Printing all key-value pairs in the dictionary
print(std.items())  # Output: dict_items([('(lol', 20), ('raj', 21), ('why', 40)])

print(std.keys()) #it will only give you the values of the key (the variables)
#output - (lol,raj,why)

print(std.pop("lol")) # to pop the element.
print(std)

std ["ani"]= 32 # to add a element in the list.
print(std)

std.popitem() # it removes out the last element of the list.
print(std)

#this is yur tuple
hetro = (1,2,4,5,3,4,66,22,89)
print(hetro.count(4))
print(hetro.index(5))