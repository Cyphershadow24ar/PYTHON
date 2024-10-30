files = ["planets1.txt", "planets2.txt", "planets3.txt"]

for file in files:
    try:
        with open(file, "r") as f:
            print(f"{file} opened successfully.")
    except FileNotFoundError:
        print(f"{file} is missing. Please create the file.")