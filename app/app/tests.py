"""
Samples Tests

"""
from django.test import SimpleTestCase
from app import calc


class CalcTestCase(SimpleTestCase):
    """ Tests Calc"""

    def test_add_number(self):
        res = calc.add(5, 8)
        self.assertEqual(res, 13)

    def test_substract_number(self):
        res = calc.subtract(10, 8)
        self.assertEqual(res, 2)
