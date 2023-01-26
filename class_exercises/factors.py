user_input = int(input("Enter a number: "))
num_of_factors = 1
for count in range(1, user_input+1 // 2):
    if user_input % count == 0:
        num_of_factors = num_of_factors + 1
print(num_of_factors)


