amt = int(input("Enter your amount = "))
if 0 <= amt <= 5000:
    discamt = amt - ((5/100) * amt)
    print(f"Discounted amount: {discamt}")
elif 5000 < amt <= 15000:
    discamt = amt - ((12/100) * amt)
    print(f"Discounted amount: {discamt}")
elif 15000 < amt <= 25000:
    discamt = amt - ((20/100) * amt)
    print(f"Discounted amount: {discamt}")
elif amt > 25000:
    discamt = amt - ((30/100) * amt)
    print(f"Discounted amount: {discamt}")
else:
    print("Invalid amount")