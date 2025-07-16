"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

import unittest

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_multiple_cases(self):
        test_cases = [
            (2, 3, 5),
            (-1, 1, 0),
            (0, 0, 0),
            (1.5, 2.5, 4.0),
            (-5, -3, -8)
        ]
        
        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = self.calc.add(a, b)
                self.assertEqual(result, expected)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
