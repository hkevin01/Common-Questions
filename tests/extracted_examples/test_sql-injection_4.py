"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/sql-injection.md
"""

from django.db import models

# Django ORM automatically prevents SQL injection
users = User.objects.filter(username=username, password=password)

# Raw queries with parameter substitution
from django.db import connection
cursor = connection.cursor()
cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", 
               [username, password])

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
