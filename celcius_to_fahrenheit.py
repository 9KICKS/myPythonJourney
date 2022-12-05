def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32


celcius = float(input("Enter celcius to convert to fahrenheit: "))
fahrenheit = celcius_to_fahrenheit(celcius)
# print(fahrenheit)
print(celcius, "celcius" " " "--->", fahrenheit, "fahrenheit")
