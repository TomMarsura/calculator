from unittest import TestCase
from src.calculator import Calculator

class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        self.assertEqual(self.calc.mysum(1, 2), 3)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)

    
    
if __name__ == '__main__':
    unittest.main()