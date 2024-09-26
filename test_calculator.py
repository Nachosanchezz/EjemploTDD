import unittest

from calculator import Calculator

class TestMyCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    def test_initial_value(self):
        calc = Calculator()
        self.assertEqual(0, calc.value)
    def test_add_method(self):
        self.calc.add(1,3)
        self.assertEqual(4, self.calc.value)
