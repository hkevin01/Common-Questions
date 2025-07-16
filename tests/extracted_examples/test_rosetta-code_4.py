"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/rosetta-code.md
"""

def quick_sort(arr):
    """Quick sort implementation"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
