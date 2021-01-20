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
