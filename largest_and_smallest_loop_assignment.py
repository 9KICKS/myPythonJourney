largest_number = "-inf"
smallest_number = 0
while True:
    user_input = input("Enter a number: ")

    if user_input.isdigit():
        print("Good job!")
    elif user_input.lower() == 'stop'.lower():
        break
    else:
        print("Olodo, I said enter a number")
    if smallest_number == 0:
        smallest_number = user_input
    if user_input <= smallest_number:
        smallest_number = user_input
    if largest_number == 0:
        largest_number = user_input
    elif user_input >= largest_number:
        largest_number = user_input

print("The largest number is : ", largest_number)
print("The smallest number is : ", smallest_number)
