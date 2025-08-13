# Find Maximum Value
def findMaximum(nums) -> int:
    """Returns the maximum value in the list"""
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            # swap values
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    # return last element
    return nums[-1]


print("Find Maximum Value")
nums = [10, 21, 13, 43, 35]
max = findMaximum(nums)
print("Maximum in", nums, "is", max)


# Find Minimum Value
def findMinimum(nums) -> int:
    """Returns the minimum value in the list"""
    for i in range(len(nums) - 1):
        if nums[i] < nums[i + 1]:
            # swap values
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
    
    # return last element
    return nums[-1]


print("Find Minimum Value")
nums = [13, 21, 10, 43, 35]
max = findMinimum(nums)
print("Minimum in", nums, "is", max)


# Find Minimum Index
def findMinimumIndex(items: list) -> int:
    """Returns the minimum index in the list"""
    size = len(items)
    minIndex = 0
    if size > 1:
        for i in range(1, size):
            if items[minIndex] > items[i]:
                minIndex = i
    
    return minIndex


print("Find Minimum Index")
nums = [13, 21, 10, 43, 35]
minIndex = findMinimumIndex(nums)
print("Minimum Index in", nums, "is", minIndex, "and value is", nums[minIndex])
