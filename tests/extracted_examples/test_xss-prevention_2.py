"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/xss-prevention.md
"""

# Django templates auto-escape by default
# template.html: {{ user_input }}  <!-- Automatically escaped -->

# To output raw HTML (dangerous): {{ user_input|safe }}

# Safe way to output user HTML
from django.utils.html import escape

# In views
def display_content(request):
    user_content = request.GET.get('content', '')
    # Django automatically escapes template variables
    return render(request, 'display.html', {'content': user_content})

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
