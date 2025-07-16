"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
