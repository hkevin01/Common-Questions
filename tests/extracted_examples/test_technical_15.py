"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

import bcrypt
import secrets
import hashlib

def hash_password(password):
    """Securely hash a password using bcrypt"""
    # Generate salt and hash password
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(password.encode('utf-8'), salt)
    return password_hash

def verify_password(password, password_hash):
    """Verify password against stored hash"""
    return bcrypt.checkpw(password.encode('utf-8'), password_hash)

def generate_secure_token():
    """Generate cryptographically secure random token"""
    return secrets.token_urlsafe(32)

# Example usage
password = "user_password_123"
hashed = hash_password(password)
is_valid = verify_password(password, hashed)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
