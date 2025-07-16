"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/fizzbuzz.md
"""

def custom_fizzbuzz(n, rules):
    """
    Generalized FizzBuzz with custom rules
    
    Args:
        n: Upper limit for counting
        rules: List of tuples (divisor, word)
    """
    for i in range(1, n + 1):
        output = ""
        for divisor, word in rules:
            if i % divisor == 0:
                output += word
        print(output or i)

# Example: FizzBuzzBang (3->Fizz, 5->Buzz, 7->Bang)
custom_fizzbuzz(50, [(3, "Fizz"), (5, "Buzz"), (7, "Bang")])

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
