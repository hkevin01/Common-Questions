"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/fizzbuzz.md
"""

import unittest

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_output(self):
        """Test FizzBuzz generates correct output"""
        expected = ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", 
                   "11", "Fizz", "13", "14", "FizzBuzz"]
        
        result = []
        for i in range(1, 16):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
                
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
