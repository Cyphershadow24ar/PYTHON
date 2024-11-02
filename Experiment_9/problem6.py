# Create a file with the word 'donkey' (Run once)
with open("animals.txt", "w") as f:
    f.write("The donkey is a domesticated animal. Donkey can carry loads.")

# Replace 'donkey' with '$$$$$'
with open("animals.txt", "r") as f:
    content = f.read()

content = content.replace("donkey", "$$$$$")

with open("animals.txt", "w") as f:
    f.write(content)

print("The word 'donkey' has been replaced with '$$$$$'.")