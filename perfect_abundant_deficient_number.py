user_input = int(input("Enter a number: "))
num_of_factors = 1
sum_of_factors = 0
while num_of_factors < user_input:
    if user_input % num_of_factors == 0:
        sum_of_factors += num_of_factors
    num_of_factors += 1
if sum_of_factors < user_input:
    print(user_input, "is deficient")
elif sum_of_factors > user_input:
    print(user_input, "is abundant")
else:
    print(user_input, "is a perfect number")



