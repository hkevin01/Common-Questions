"""
Extracted from /home/kevin/Projects/Common-Questions/content/interview-questions/technical.md
"""

def two_sum(nums, target):
    """Find indices of two numbers that add up to target"""
    # Hash map approach - O(n) time, O(n) space
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    
    return []  # No solution found

# Two-pointer approach for sorted array
def two_sum_sorted(nums, target):
    """Find two numbers in sorted array that sum to target"""
    left, right = 0, len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

# Test function
def test_syntax():
    """Test that code compiles without syntax errors."""
    pass
