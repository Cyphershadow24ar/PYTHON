# WAP in python to print each line of a file in reverse order.

# Function to print each line of a file in reverse order
def print_lines_reverse(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        for line in lines:  # Reverse each line and print it
            print(line.strip()[::-1])
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Call the function with the filename
filename = 'example.txt'
print_lines_reverse(filename)
