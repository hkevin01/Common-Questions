"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/sql-injection.md
"""

import re
from html import escape

def validate_input(input_data, input_type):
    """Validate and sanitize input based on type"""
    if input_type == 'email':
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, input_data) is not None
    elif input_type == 'username':
        pattern = r'^[a-zA-Z0-9_]{3,20}$'
        return re.match(pattern, input_data) is not None
    elif input_type == 'integer':
        try:
            int(input_data)
            return True
        except ValueError:
            return False
    return False

def sanitize_string(input_string):
    """Sanitize string input by removing dangerous characters"""
    # Remove or escape potentially dangerous characters
    dangerous_chars = ['\'', '"', ';', '\\', '<', '>', '&']
    for char in dangerous_chars:
        input_string = input_string.replace(char, '')
    return input_string.strip()

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
