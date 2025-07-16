"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Add item to top of stack - O(1)"""
        self.items.append(item)
    
    def pop(self):
        """Remove and return top item - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top item without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def is_empty(self):
        """Check if stack is empty - O(1)"""
        return len(self.items) == 0
    
    def size(self):
        """Return number of items - O(1)"""
        return len(self.items)

# Use cases:
# - Function call management (call stack)
# - Undo operations in applications
# - Expression evaluation and syntax parsing
# - Browser history (back button)
# - Depth-First Search (DFS) algorithms

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
