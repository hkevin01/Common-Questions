"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

class Calculator:
    """A simple calculator for basic arithmetic operations."""
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and return the result."""
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a and return the result."""
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and return the result."""
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
