"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

def update_user(user_id, data):
    # Update database
    database.update_user(user_id, data)
    # Update cache
    cache.set(f"user:{user_id}", data, ttl=3600)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
