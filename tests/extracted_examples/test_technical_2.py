"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

def animal_sound(animal):
    return animal.speak()  # Same method, different behavior

animals = [Dog("Buddy"), Cat("Whiskers")]
for animal in animals:
    print(animal_sound(animal))  # Polymorphic behavior

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
