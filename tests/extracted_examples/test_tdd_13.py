"""
Extracted from /home/kevin/Projects/Common-Questions/content/development-practices/tdd.md
"""

# Bad: Testing internal implementation
def test_sort_uses_quicksort_algorithm(self):
    sorter = Sorter()
    # This test breaks if we change the algorithm
    self.assertEqual(sorter.algorithm_used, "quicksort")

# Good: Testing behavior
def test_sort_returns_ascending_order(self):
    sorter = Sorter()
    result = sorter.sort([3, 1, 4, 1, 5])
    self.assertEqual(result, [1, 1, 3, 4, 5])

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
