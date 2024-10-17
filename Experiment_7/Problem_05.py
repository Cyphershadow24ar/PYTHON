# Global variable, taking input from the user
x = int(input("Enter a value for global x: "))

def outer_function():
    # Enclosing variable, taking input from the user
    x = int(input("Enter a value for enclosing x (inside outer_function): "))

    def inner_function():
        # Local variable, taking input from the user
        x = int(input("Enter a value for local x (inside inner_function): "))
        print(f"Local x (inner_function): {x}")  # Access local x

    inner_function()
    print(f"Enclosing x (outer_function): {x}")  # Access enclosing x

# Access global variable
print(f"Global x: {x}")
outer_function()
print(f"Global x after outer_function: {x}")
