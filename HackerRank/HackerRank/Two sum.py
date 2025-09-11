def two_sum(nums, target):
    indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in indices:
            return [indices[complement], i]
        indices[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9

result = two_sum(nums, target)
print(result)  # [0, 1]


















































































