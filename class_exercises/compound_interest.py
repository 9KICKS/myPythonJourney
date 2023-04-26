principal = int(input("Enter your principal: "))
year = int(input("Enter projected years: "))
rate = 0.05
print("  Year           Amount")
for i in range(1, year + 1):
    amount = principal * (1.0 + rate) * i
    print("{:4d}{:20,.2f}".format(i, amount))
