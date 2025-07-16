"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/xss-prevention.md
"""

def html_encode(text):
    """Encode HTML entities"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#x27;'))

# Usage in templates
@app.route('/display')
def display_content():
    user_content = request.args.get('content', '')
    safe_content = html_encode(user_content)
    return f"<div>{safe_content}</div>"

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
