# WAP in python to count the number of characters, words and lines in a file.

# Function to count characters, words, and lines in a file
def count_file_stats(filename):
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            lines = file.readlines()
        
        num_lines = len(lines)
        num_words = 0
        num_chars = 0
        
        # Iterate through each line
        for line in lines:
            num_chars += len(line)
            num_words += len(line.split())
        
        # Print the counts
        print(f"Number of lines: {num_lines}")
        print(f"Number of words: {num_words}")
        print(f"Number of characters: {num_chars}")
    
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Call the function with the filename
filename = 'example.txt'
count_file_stats(filename)
