import time


def validator(card_number):
    reversed_digits = [int(x) for x in card_number][::-1]
    doubled_digits = [x * 2 if i % 2 == 0 else x for i, x in enumerate(reversed_digits)]
    subtracted_digits = [x - 9 if x > 9 else x for x in doubled_digits]
    total = sum(subtracted_digits)
    if total % 10 == 0:
        return "Invalid credit card"
    else:
        return "Valid credit card"


credit_card = str(input("Hello, kindly enter card details to verify: "))
print()
print("Verifying ")
time.sleep(2.0)
print(">>>>>>>>>>")
time.sleep(1.0)
print(">>>>>>>>>>")
time.sleep(1.0)
print(">>>>>>>>>>")
print("Verification Complete!")
print()


def credit_card_type():
    if credit_card[0] == "4":
        return "Visa Card"
    elif credit_card[0] == "5":
        return "Mastercard"
    elif credit_card[0] == "3":
        return "American Express Card"
    elif credit_card[0] == "6":
        return "Discover Card"
    else:
        return "Invalid card type"


card_type = str(credit_card_type())
card_length = str(len(credit_card))

print("*****************************************************")
print("** Credit Card Type: " + card_type)
print("** Credit Card Number: " + credit_card)
print("** Credit Card Digit Length: " + card_length)
print("** Credit Card Validity Status: " + validator(credit_card))
print("*****************************************************")
