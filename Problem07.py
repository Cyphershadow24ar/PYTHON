#Enter a paragraph and display the sub-string by using string slicing.
# Define the paragraph
paragraph = """A data structure is a specialized format for organizing, processing, retrieving and storing data.
The logical or mathematical model of a particular organization of data is called data structure."""

# Extract the first 20 characters
first_20_chars = paragraph[:20]
print("First 20 characters:", first_20_chars)

# Extract characters from index 30 to 50
chars_30_to_50 = paragraph[30:50]
print("\nCharacters from index 30 to 50:", chars_30_to_50)

# Extract the last 20 characters
last_20_chars = paragraph[-20:]
print("\nLast 20 characters:", last_20_chars)

# Extract every 3rd character from the paragraph
every_3rd_char = paragraph[::3]
print("\nEvery 3rd character:", every_3rd_char)
