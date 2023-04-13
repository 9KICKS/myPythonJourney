def get_highest_common_factor(user_numbers, **kwargs):
    first_default_value = 0
    second_default_value = 0
    first_argument = kwargs.get('arg1', first_default_value)
    second_argument = kwargs.get('arg2', second_default_value)
    if len(user_numbers) == 0:
        return None
    highest_common_factor = user_numbers[0]
    for number in user_numbers:
        highest_common_factor = get_greatest_common_divisor(highest_common_factor, number)
    return get_prime_factors(highest_common_factor)


def get_greatest_common_divisor(x, y):
    if y == 0:
        return x
    return get_greatest_common_divisor(y, x % y)


def get_prime_factors(number):
    i = 2
    factors = []
    while i <= number:
        if number % i == 0:
            number //= i
            factors.append(i)
        else:
            i += 1
    if number > 1:
        factors.append(number)
    return factors


user_input = list(map(int, input("Enter multiple numbers separated by a ',': ").split(",")))
result = get_highest_common_factor(user_input, arg1=1000, arg2=100)
print(result)
