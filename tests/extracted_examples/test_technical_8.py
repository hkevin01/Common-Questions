"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

def get_user(user_id):
    # Check cache first
    user = cache.get(f"user:{user_id}")
    if user is None:
        # Cache miss - fetch from database
        user = database.get_user(user_id)
        # Store in cache
        cache.set(f"user:{user_id}", user, ttl=3600)
    return user

def update_user(user_id, data):
    # Update database
    database.update_user(user_id, data)
    # Invalidate cache
    cache.delete(f"user:{user_id}")

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
