# Input principal amount, rate of interest, and interest

PA = int(input("Enter the Principal Amount: ₹"))
SI = int(input("Enter the Interest: ₹"))
RI = float(input("Enter the Rate of Interest (%): "))

# Calculate the time
Time = (SI * 100) / (PA * RI)

print(f"The total time is {Time} years.")

