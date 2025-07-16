"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/xss-prevention.md
"""

import html
import re
from bleach import clean

def sanitize_input(user_input):
    """Sanitize user input to prevent XSS"""
    # HTML escape
    escaped = html.escape(user_input)
    
    # Remove dangerous patterns
    dangerous_patterns = [
        r'<script.*?</script>',
        r'javascript:',
        r'on\w+\s*=',  # event handlers like onclick, onload
        r'<iframe.*?</iframe>',
        r'<object.*?</object>',
        r'<embed.*?</embed>'
    ]
    
    for pattern in dangerous_patterns:
        escaped = re.sub(pattern, '', escaped, flags=re.IGNORECASE | re.DOTALL)
    
    return escaped

# Using bleach library for HTML sanitization
def clean_html_content(content):
    """Clean HTML content, allowing only safe tags"""
    allowed_tags = ['p', 'b', 'i', 'u', 'em', 'strong', 'a', 'ul', 'ol', 'li']
    allowed_attributes = {'a': ['href', 'title']}
    
    return clean(content, tags=allowed_tags, attributes=allowed_attributes)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
