from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are effectively added together"""
        self.assertEqual(add(2, 12), 14)

    def test_subtract_numbers(self):
        """Test that values are subtract and returned"""
        self.assertEqual(subtract(3, 10), 7)