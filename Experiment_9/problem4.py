# Create planets.txt with some data (Run once)
with open("planets.txt", "w") as f:
    f.write("Mercury\nVenus\nEarth\nMars\nJupiter\nSaturn\nUranus\nNeptune")

# Wipe out the content of planets.txt
with open("planets.txt", "w") as f:
    f.truncate(0)  # Truncate the file to 0 bytes

print("Contents of planets.txt have been wiped out.")