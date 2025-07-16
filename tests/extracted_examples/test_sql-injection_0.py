"""
Extracted from /home/kevin/Projects/Common-Questions/content/web-security/sql-injection.md
"""

import sqlite3

# Vulnerable code
username = request.form['username']
password = request.form['password']
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

# Secure code with parameterized queries
username = request.form['username']
password = request.form['password']
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
