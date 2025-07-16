"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

# Good: Single responsibility
def test_user_creation_sets_name(self):
    user = User("John")
    self.assertEqual(user.name, "John")

def test_user_creation_sets_default_age(self):
    user = User("John")
    self.assertEqual(user.age, 0)

# Avoid: Multiple assertions testing different things
def test_user_creation(self):
    user = User("John")
    self.assertEqual(user.name, "John")  # Testing name
    self.assertEqual(user.age, 0)        # Testing age
    self.assertTrue(user.is_active)      # Testing status

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
