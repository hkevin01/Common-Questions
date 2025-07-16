"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

import string
import random

def generate_short_url(length=7):
    """Generate random short URL"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

def base62_encode(num):
    """Convert number to base62 string"""
    if num == 0:
        return '0'
    
    chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while num > 0:
        result = chars[num % 62] + result
        num //= 62
    
    return result

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
