# Write a program in python to demonstrate different types of 
# exceptions and errors.

def demonstrate_exceptions():
    print("1. ZeroDivisionError")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")

    print("\n2. ValueError")
    try:
        number = int("not_a_number")
    except ValueError as e:
        print(f"Error: {e}")

    print("\n3. IndexError")
    try:
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError as e:
        print(f"Error: {e}")

    print("\n4. KeyError")
    try:
        d = {"key1": "value1"}
        print(d["key2"])
    except KeyError as e:
        print(f"Error: {e}")

    print("\n5. FileNotFoundError")
    try:
        with open("non_existent_file.txt", "r") as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")

    print("\n6. TypeError")
    try:
        result = "string" + 5
    except TypeError as e:
        print(f"Error: {e}")

    print("\n7. AttributeError")
    try:
        number = 10
        number.append(5)  # Integers don't have an 'append' method
    except AttributeError as e:
        print(f"Error: {e}")

    print("\n8. ImportError")
    try:
        import non_existent_module
    except ImportError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    demonstrate_exceptions()
