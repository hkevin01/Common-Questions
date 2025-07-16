"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

# Array characteristics:
# - Contiguous memory allocation
# - O(1) random access by index
# - O(n) insertion/deletion (except at end)
# - Better cache locality

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self, data):  # O(1)
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, data):  # O(n)
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

# Linked List characteristics:
# - Non-contiguous memory allocation
# - O(n) access by position
# - O(1) insertion/deletion at known position
# - Dynamic size, no memory waste

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
