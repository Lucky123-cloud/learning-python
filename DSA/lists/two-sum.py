def two_sum(nums, target):
    lookup = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in lookup:
            return [lookup[complement], i]
        
        lookup[num] = i


# OR

def two_sum2(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            

print(two_sum([2, 7, 11, 15], 9))
print(two_sum2([2, 7, 11, 15, 9], 9))
