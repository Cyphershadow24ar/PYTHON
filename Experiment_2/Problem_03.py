#Write a Python program to input your name and reverse it. Print last 5 character of reversed name.

name = (input("Enter you name: "))

reverse = name[::-1]
last_5_Character = reverse[-5:]

print(f"The reverse of the given name is {reverse}.")
print(f"last 5 character of reversed name is {last_5_Character}.")

