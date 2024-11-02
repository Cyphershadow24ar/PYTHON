# Creating poems.txt file (Run this part only once to create the file)
with open("poems.txt", "w") as f:
    f.write("Twinkle, twinkle, little star,\nHow I wonder what you are!")

# Checking if the words "twinkle" and "star" are present
with open("poems.txt", "r") as f:
    content = f.read().lower()  # Convert to lowercase for case-insensitive search

if "twinkle" in content and "star" in content:
    print("Both 'twinkle' and 'star' are present in the poem.")
else:
    print("'twinkle' or 'star' is missing.")