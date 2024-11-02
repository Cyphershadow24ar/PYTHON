import os

# Create a sample file to rename (Run once)
with open("sample_file.txt", "w") as f:
    f.write("This is a sample file.")

# Rename the file
os.rename("sample_file.txt", "renamed_by_python.txt")
print("File renamed to 'renamed_by_python.txt'.")