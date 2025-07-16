"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

import unittest

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        calc = Calculator()
        result = calc.add(2, 3)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
