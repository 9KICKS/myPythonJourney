count = 0
while count < 5:
    user_input = int(input("Give me a number: "))

def soution(input):
    largest = input(0)
    second_largest = input(0)
    smallest = input(0)

    for ls in input:
        if ls > largest:
            largest = ls

        if ls < smallest:
            smallest = ls

    for ls in input:
        if ls > second_largest & ls < largest:
            second_largest = ls

    print("Largest is: ", 'largest')
    print("Second largest is: ", second_largest)
    print("Smallest is: ", smallest)