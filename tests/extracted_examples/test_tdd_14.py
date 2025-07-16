"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

# Bad: Complex test setup
def test_complex_scenario(self):
    # 20 lines of setup code
    # Multiple objects and interactions
    # Hard to understand what's being tested
    pass  # Implementation would be complex

# Good: Simple, focused test
def test_user_can_login_with_valid_credentials(self):
    user = User("john@example.com", "password123")
    result = user.login("john@example.com", "password123")
    self.assertTrue(result)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
