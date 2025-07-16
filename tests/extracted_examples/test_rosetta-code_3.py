"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/rosetta-code.md
"""

def bubble_sort(arr):
    """Bubble sort implementation"""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
