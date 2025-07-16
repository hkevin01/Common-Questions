"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/xss-prevention.md
"""

import re

def validate_user_input(input_data, input_type):
    """Validate user input based on expected type"""
    
    validators = {
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
        'username': r'^[a-zA-Z0-9_]{3,20}$',
        'phone': r'^\+?1?-?\.?\s?\(?[0-9]{3}\)?[\s.-]?[0-9]{3}[\s.-]?[0-9]{4}$',
        'alphanumeric': r'^[a-zA-Z0-9\s]+$'
    }
    
    if input_type in validators:
        return bool(re.match(validators[input_type], input_data))
    
    return False

# Usage
email = "user@example.com"
if validate_user_input(email, 'email'):
    # Process valid email
    pass

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
