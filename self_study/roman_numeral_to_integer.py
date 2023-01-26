def roman_to_integer(number):
    roman_dictionary = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for i in range(len(number)):
        if i > 0 and roman_dictionary[number[i]] > roman_dictionary[number[i - 1]]:
            value += roman_dictionary[number[i]] - 2 * roman_dictionary[number[i - 1]]
        else:
            value += roman_dictionary[number[i]]
    return value


user_roman_numeral = str(input("Enter a roman numeral: "))
print(user_roman_numeral, "-> integer =", roman_to_integer(user_roman_numeral.upper()))
