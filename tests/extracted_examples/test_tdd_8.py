"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

# Start simple
def test_empty_list_has_zero_length(self):
    my_list = MyList()
    self.assertEqual(len(my_list), 0)

# Then add complexity
def test_add_item_increases_length(self):
    my_list = MyList()
    my_list.add("item")
    self.assertEqual(len(my_list), 1)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
