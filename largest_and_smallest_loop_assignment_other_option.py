user_input = int(input("Enter a number (Punch 0 to stop"))
largest_number = smallest_number = user_input
while user_input != 0:
    if user_input > largest_number:
        largest_number = user_input
    if user_input < smallest_number:
        smallest_number = user_input
    user_input = int(input("Enter a number (Punch 0 to stop"))

    print("Largest is ", largest_number)
    print("Smallest is ", smallest_number)
