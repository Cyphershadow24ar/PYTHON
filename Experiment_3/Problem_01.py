# Using if-else statement Write a Python program to perform an ATM operation by inputting an amount to withdraw which should be multiple of 100 (Money should be withdrawal in terms of 100, 200, 500,2000). Follow te process below.
# Case1: amount to be withdrawal is 4500 which is multiple of 100. Then it will print Please take 2 notes of 2000 Rupees, 1 note of 500 rupees.
# Case2: amount to be withdrawal is 9800 which is multiple of 100. Then it will print Please take 4 notes of 2000 Rupees, 3 notes of 500 rupees, 1 note of  200 rupees, 1 note of 100 rupees.
# Case3: amount to be withdrawal is 1800 which is multiple of 100. Then it will print Please take 3 notes of 500 rupees, 1 note of  200 rupees, 1 note of 100 rupees.
# Case4: amount to be withdrawal is 800 which is multiple of 100. Then it will print Please take 1 note of 500 rupee, 1 note of  200 rupee, 1 note of 100 rupee.
# Case5: amount to be withdrawal is 800 which is multiple of 100. Then it will print Please take 1 note of 500 rupee, 1 note of 200 rupees, 1 note of 100 rupees.
# Case6: amount to be withdrawal is 300 which is multiple of 100. Then it will print Please take 1 note of  200 rupee, 1 note of 100 rupee
# Case7: amount to be withdrawal is 100 which is multiple of 100. Then it will print Please take  1 note of 100 rupees.

# Input the amount to withdraw
amount = int(input("Enter the amount to withdraw (must be a multiple of 100): "))

# Initialize counters for each denomination
notes_2000 = notes_500 = notes_200 = notes_100 = 0

# Check if the amount is a multiple of 100
if amount % 100 != 0:
    print("Invalid amount. Please enter an amount that is a multiple of 100.")
else:
    # Calculate the number of 2000 rupee notes
    if amount >= 2000:
        notes_2000 = amount // 2000
        amount = amount % 2000

    # Calculate the number of 500 rupee notes
    if amount >= 500:
        notes_500 = amount // 500
        amount = amount % 500

    # Calculate the number of 200 rupee notes
    if amount >= 200:
        notes_200 = amount // 200
        amount = amount % 200

    # Calculate the number of 100 rupee notes
    if amount >= 100:
        notes_100 = amount // 100

    # Prepare the output message
    output = "Please take "
    if notes_2000 > 0:
        output += f"{notes_2000} notes of 2000 Rupees, "
    if notes_500 > 0:
        output += f"{notes_500} notes of 500 Rupees, "
    if notes_200 > 0:
        output += f"{notes_200} notes of 200 Rupees, "
    if notes_100 > 0:
        output += f"{notes_100} notes of 100 Rupees, "

    # Remove the trailing comma and space, then print the result
    output = output.rstrip(', ')
    print(output)
