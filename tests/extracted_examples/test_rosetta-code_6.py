"""
Extracted from /home/kevin/Projects/Common-Questions/content/coding-challenges/rosetta-code.md
"""

def are_anagrams(str1, str2):
    """Check if two strings are anagrams"""
    # Remove spaces and convert to lowercase
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    
    # Sort characters and compare
    return sorted(str1) == sorted(str2)

# Alternative using character count
from collections import Counter
def are_anagrams_counter(str1, str2):
    str1 = str1.replace(' ', '').lower()
    str2 = str2.replace(' ', '').lower()
    return Counter(str1) == Counter(str2)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
