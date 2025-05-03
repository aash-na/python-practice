# Problem: Find the contiguous subarray which has the largest sum and return its sum.

def max_sub_array(nums):
    """
    Find the maximum sum of a contiguous subarray.

    Args:
    nums (list of int): List of integers

    Returns:
    int: Maximum sum of contiguous subarray
    """
    max_sum = current_sum = nums[0]
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage:
print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
