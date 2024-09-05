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
