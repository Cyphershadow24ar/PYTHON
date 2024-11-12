# Write a program in python to demonstrate Try, Except with Finally block
# What is the need of finally block in python explain this.

def demonstrate_try_except_finally():
    try:
        print("Trying to open a file...")
        # Attempt to open a file that does not exist
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Exception caught: {e}")
    finally:
        print("Finally block executed: Cleaning up resources or finalizing tasks.")

# Run the demonstration
demonstrate_try_except_finally()
