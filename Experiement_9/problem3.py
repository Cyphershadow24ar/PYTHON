# Create Galaxy.txt with sample data (Run once)
with open("Galaxy.txt", "w") as f:
    f.write("Andromeda\nMilky Way\nTriangulum\nWhirlpool\n...\n")  # Add more names

# Copy content from Galaxy.txt to a new file named Galaxy_copy.txt
with open("Galaxy.txt", "r") as source:
    content = source.read()

with open("Galaxy_copy.txt", "w") as destination:
    destination.write(content)

print("Galaxy.txt copied to Galaxy_copy.txt successfully.")