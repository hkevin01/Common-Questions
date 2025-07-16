"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()
    
    def test_divide_by_zero_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        
        self.assertEqual(str(context.exception), "Cannot divide by zero")
    
    def test_divide_by_zero_specific_message(self):
        with self.assertRaisesRegex(ValueError, "Cannot divide by zero"):
            self.calc.divide(5, 0)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
