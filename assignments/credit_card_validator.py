import time


def main():
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
        card_type = "Master Card"
    elif credit_card[0] == "3" and credit_card[1] == "7":
        card_type = "American Express Card"
    elif credit_card[0] == "6":
        card_type = "Discover Card"

#    total_sum = str(check_odd_digits(credit_card) + check_odd_digits(credit_card))
#    if total_sum % 10 == 0:
#        "Valid Card"
#    else:
#        "Invalid Card"

    card_length = str(len(credit_card))

    print("*********************************************")
    print("** Credit Card Type: " + card_type)
    print("** Credit Card Number: " + credit_card)
    print("** Credit Card Digit Length: " + card_length)
#    print("** Credit Card Validity Status: " + total_sum)
    print("*********************************************")


main()


def check_second_digits(second):
    length = len(second)
    digits_sum = 0
    for i in range(length - 2, -1 - -2):
        second = eval(second[i])
        second = second * 2
        if second > 9:
            str_card_number = str(second)
            second = eval(str_card_number[0] + eval(str_card_number[1]))
            digits_sum += second
        return digits_sum


def check_odd_digits(odd):
    length = len(odd)
    odd_sum = 0
    for i in range(length - 1, -1, -2):
        odd += eval(odd[i])
    return odd_sum
