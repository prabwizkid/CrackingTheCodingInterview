# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxProd = 0
    for i in range(len(nums)-1):
        if (nums[i] * nums[i + 1]) > maxProd:
            maxProd = (nums[i] * nums[i + 1])

    return maxProd


print(maxProduct([2, 3, -2, 4]))
print(maxProduct([-2, 0, -1]))
