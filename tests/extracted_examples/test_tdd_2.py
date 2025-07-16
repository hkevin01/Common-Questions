"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_add_two_numbers(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_add_negative_numbers(self):
        result = self.calc.add(-1, -2)
        self.assertEqual(result, -3)
    
    def test_subtract_two_numbers(self):
        result = self.calc.subtract(5, 3)
        self.assertEqual(result, 2)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
