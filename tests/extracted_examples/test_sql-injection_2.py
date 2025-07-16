"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/sql-injection.md
"""

def validate_data_types(data):
    """Validate data types before database operations"""
    
    validations = {
        'user_id': lambda x: isinstance(x, int) and x > 0,
        'email': lambda x: isinstance(x, str) and '@' in x and len(x) < 255,
        'age': lambda x: isinstance(x, int) and 0 <= x <= 150,
        'username': lambda x: isinstance(x, str) and x.isalnum() and 3 <= len(x) <= 20
    }
    
    for field, value in data.items():
        if field in validations:
            if not validations[field](value):
                raise ValueError(f"Invalid {field}: {value}")
    
    return True

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
