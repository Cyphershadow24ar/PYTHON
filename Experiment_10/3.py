try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the filename.")
finally:
    print("Closing file if it was opened.")
    if 'file' in locals():
        file.close()