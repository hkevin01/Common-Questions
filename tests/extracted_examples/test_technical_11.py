"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

def is_palindrome(s):
    """Check if string is palindrome (case-insensitive, alphanumeric only)"""
    # Clean string: remove non-alphanumeric, convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Two-pointer approach
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
test_cases = [
    "A man a plan a canal Panama",  # True
    "race a car",                   # False
    "hello",                        # False
    "Madam",                        # True
    ""                              # True (empty string)
]

for test in test_cases:
    print(f"'{test}' -> {is_palindrome(test)}")

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
