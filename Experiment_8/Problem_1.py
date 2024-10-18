#WAP in python to count frequency of characters in a file.

# Function to count frequency of characters in a file
def count_char_frequency(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            text = file.read()
        
        # Create an empty dictionary to store the frequency of characters
        frequency = {}
        
        # Count the frequency of each character in the file
        for char in text:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        # Print the frequency of each character
        print("Character frequencies:")
        for char, count in frequency.items():
            print(f"{char}: {count}")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Call the function with the filename
filename = 'example.txt'
count_char_frequency(filename)
