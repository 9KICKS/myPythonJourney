def celsius_to_fahrenheit(c):
    return c * 1.8 + 32


celsius = float(input("Enter celsius to convert to fahrenheit: "))
fahrenheit = celsius_to_fahrenheit(celsius)
# print(fahrenheit)
print(celsius, "celsius" " " "--->", fahrenheit, "fahrenheit")
