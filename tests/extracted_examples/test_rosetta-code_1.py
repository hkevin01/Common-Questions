"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/rosetta-code.md
"""

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Iterative approach (more efficient)
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Generate first 10 Fibonacci numbers
print(list(fibonacci_iterative(10)))

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
