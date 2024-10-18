# WAP in python to read an entire text file.

# Function to read the entire content of a file
def read_file(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
        
        # Print the file content
        print(content)
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Call the function with the filename
filename = 'example.txt'
read_file(filename)
