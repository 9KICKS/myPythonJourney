def kilograms_to_pounds(kilograms):
    return kilograms * 2.2


print("Kilograms            Pounds")
for i in range(1, 201, 2):
    print(str(i) + " " * 20 + str(round(kilograms_to_pounds(i), 2)))
