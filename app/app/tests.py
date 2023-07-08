"""
Sample Test Runner
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        res = calc.add(5, 5)
        self.assertEquals(res, 10)
