def twosum(nums, target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in seen:
            return[seen[complement],i]
        seen[nums[i]] = i

       
print(twosum([2,7,11,15], 9))
print(twosum([3,2,4], 6))
print(twosum([3,3], 6)) 
            