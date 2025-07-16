"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

class TestStringValidator(unittest.TestCase):
    def test_empty_string_is_invalid(self):
        self.assertFalse(is_valid_name(""))
    
    def test_single_character_is_valid(self):
        self.assertTrue(is_valid_name("A"))
    
    def test_max_length_string_is_valid(self):
        max_name = "A" * 50  # Assuming max length is 50
        self.assertTrue(is_valid_name(max_name))
    
    def test_over_max_length_string_is_invalid(self):
        too_long_name = "A" * 51
        self.assertFalse(is_valid_name(too_long_name))

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
