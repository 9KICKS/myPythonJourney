def int_to_roman(number):
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman_numeral = ''
    i = 0
    while number > 0:
        for _ in range(number // value[i]):
            roman_numeral += symbol[i]
            number -= value[i]
        i += 1
    return roman_numeral


user_integer = int(input("Enter an integer: "))
print(user_integer, "-> roman numeral =", int_to_roman(user_integer))
