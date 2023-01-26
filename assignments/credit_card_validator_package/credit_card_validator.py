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
card_type = ""
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

if credit_card[0] == "4":
    card_type = "Visa Card"
elif credit_card[0] == "5":
    card_type = "Mastercard"
elif credit_card[0] == "3":
    card_type = "American Express Card"
elif credit_card[0] == "6":
    card_type = "Discover Card"
else:
    "Invalid card type"

card_length = str(len(credit_card))

print("*****************************************************")
print("** Credit Card Type: " + card_type)
print("** Credit Card Number: " + credit_card)
print("** Credit Card Digit Length: " + card_length)
print("** Credit Card Validity Status: " + validator(credit_card))
print("*****************************************************")
