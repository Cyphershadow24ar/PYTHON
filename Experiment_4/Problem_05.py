# wap to input a lowercase string from user and convert it into 
# upper case without using inbuilt function.

# Input lowercase string from user
lcs= input("Enter a lowercase string: ")

ucs = "" # Initialize an empty string to store the uppercase result

for char in lcs: # Loop through each character in the input string
    
    if ('a' <= char <= 'z'): # Check if the character is a lowercase letter
        ucs += chr(ord(char) - 32) # Convert to uppercase by subtracting 32 from its ASCII value
    else:
        ucs += char  # If not a lowercase letter, keep the character unchanged

print("Uppercase string:", ucs) # Print the result
