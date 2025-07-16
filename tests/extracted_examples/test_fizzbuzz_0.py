"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/fizzbuzz.md
"""

def fizzbuzz():
    """
    Classic FizzBuzz implementation
    """
    for i in range(1, 101):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Alternative using string concatenation
def fizzbuzz_alternative():
    """
    Alternative implementation using string building
    """
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        print(output or i)

if __name__ == "__main__":
    fizzbuzz()

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
