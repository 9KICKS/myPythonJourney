capital_cities = {"Nigeria": "Abuja", "Ghana": "Accra", "South Africa": "Pretoria"}
print(capital_cities)

print()

numbers = {1: "One", 2: "Two", 3: "Three"}
print(numbers)
numbers[4] = "Four"
print("Updated Dictionary: ", numbers)

print()

# To add to a dictionary:
capital_cities = {"Nigeria": "Abuja", "Ghana": "Accra", "South Africa": "Pretoria"}
print("Initial Dictionary :", capital_cities)

capital_cities["Senegal"] = "Dakar"
print("Updated Dictionary: ", capital_cities)

print()

# To change values in a dictionary:
numbers[2] = "II"
print("Replaced Dictionary: ", numbers)

print()

# Accessing elements in a dictionary:
print(capital_cities["Nigeria"])

print()

# To remove elements in a dictionary:
del numbers[4]
print("Updated Dictionary: ", numbers)
