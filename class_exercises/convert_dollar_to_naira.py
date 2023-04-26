# user_amount = int(input("Enter your amount ($): "))
# convert = user_amount * 462
# print("{} -> ₦ = {:,.0f}".format(user_amount, convert))
# print(f"Your $ amount -> ₦ = {convert:,.2f}")

def naira_converter():
    user_amount = int(input("Enter your amount ($): "))
    convert = user_amount * 462
    print("{} -> ₦ = {:,.0f}".format(user_amount, convert))
    return convert


naira_converter()
