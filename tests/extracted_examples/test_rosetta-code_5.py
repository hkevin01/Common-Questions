"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/rosetta-code.md
"""

def is_palindrome(s):
    """Check if string is a palindrome (ignoring case and non-alphanumeric)"""
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

# Test cases
test_strings = ["A man a plan a canal Panama", "race a car", "hello"]
for s in test_strings:
    print(f"'{s}' is palindrome: {is_palindrome(s)}")

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
