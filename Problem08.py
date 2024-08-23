#WAP to enter your name and print after deleting first and last characters of the name.

name = input("Enter the name: ")

if len(name)>2:
    new_name= name[1:-1]
    print(f"Name after deleting the first and last characters: {new_name}")
else:
    print("Name is too short to remove the first and last Characters.")