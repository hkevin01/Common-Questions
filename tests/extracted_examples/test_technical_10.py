"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

def update_user(user_id, data):
    # Update cache immediately
    cache.set(f"user:{user_id}", data, ttl=3600)
    # Queue database update for later
    queue.add_task("update_user_db", user_id, data)

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
