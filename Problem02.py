# WAP to input principal amount, rate of interest and time then calculate simple interest and cumulative interest.

PA = int(input("Enter the Principal Amount: ₹"))
RI = float(input("Enter the Rate of interest(%): "))
T = int(input("Enter the Time: "))

SI = ((PA * RI * T)/100)
print(f"The Simple Interest earned over {T} years would be ₹{SI}.")

