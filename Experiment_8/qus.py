# WAP in python to count frequency of characters.

name = input("Enter the any amount of characters: ")
str = "i"
# me = name.count(str) #find the given str no.
# me = name.strip() # remove the spaces from the given input
# me = name.split() # splits it and enter it in a loop !
# me  = name.startswith(str) # return true is str = input or else : false
# me = name.endswith(str) # vise versa of startswith
me = name.encode(str) #  returns the encoded from, based on the given encoding scheme
me = name.decode(str) # returns the decoded string s, based on the encoding scheme
print(me)

