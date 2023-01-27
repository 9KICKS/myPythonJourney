import unittest

from credit_card_validator import validator


class TestCreditCardValidator(unittest.TestCase):

    def test_valid_credit_card(self):
        self.assertEqual(validator("5399834432138592"), "Valid credit card")

    def test_invalid_credit_card(self):
        self.assertEqual(validator("539983443213859"), "Valid credit card")


if __name__ == '__main__':
    unittest.main()
