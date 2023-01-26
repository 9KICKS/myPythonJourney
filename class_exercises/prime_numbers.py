user_input = int(input("Enter a number: "))
prime_number = 1
for count in range(1, user_input+1 // 2):
    if user_input % count == 0:
        print(user_input, "is not a prime number")
        break
    else:
        print(user_input, " is a prime number")
