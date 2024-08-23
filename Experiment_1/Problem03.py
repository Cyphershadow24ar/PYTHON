# WAP to input principal amount, interest and time then calculate rate of interest.

PA = int(input("Enter the Principal Amount: ₹"))
SI = float(input("Enter the interest: ₹"))
T = int(input("Enter the Time: "))

RI = ((SI*100)/(PA*T))
print(f"The Rate of Interest would be % {RI}.")

