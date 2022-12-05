count = 0
largest_number = float("-inf")
smallest_number = float("+inf")
second_largest = 0

while count < 5:
    user_input = int(input("Enter numbers: "))
    if user_input > largest_number:
        second_largest = largest_number
        largest_number = user_input

    if second_largest < user_input < largest_number:
        second_largest = user_input

    if user_input < smallest_number:
        smallest_number = user_input

    count += 1
print("The largest number is ", largest_number)
print("The smallest number is ", smallest_number)
print("The second largest number is ", second_largest)
