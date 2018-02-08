from unittest import TestCase

from convert_numbers import make_numeral


class TestNumerals(TestCase):
    def test_one_returns_numeral_I(self):
        numeral = make_numeral(1)
        self.assertEqual('I', numeral)

    def test_three_returns_numeral_III(self):
        numeral = make_numeral(3)
        self.assertEqual('III', numeral)

    def test_nine_returns_numeral_IX(self):
        numeral = make_numeral(9)
        self.assertEqual('IX', numeral)

    def test_one_thousand_sixty_six_returns_numeral_MLXVI(self):
        numeral = make_numeral(1066)
        self.assertEqual('MLXVI', numeral)

    def test_nineteen_eighty_nine_returns_numeral_MCMLXXXIX(self):
        numeral = make_numeral(1989)
        self.assertEqual('MCMLXXXIX', numeral)

    def test_zero_returns_exception(self):
        with self.assertRaises(Exception) as context:
            make_numeral(0)
        self.assertTrue('There is no Roman numeral for zero' in str(context.exception))

    def test_negative_returns_exception(self):
        with self.assertRaises(Exception) as context:
            make_numeral(-5)
        self.assertTrue('There are no negative Roman numerals' in str(context.exception))
