def nextpermut(nums):
    i = len(nums) - 2
    while i>= 0  and nums[i] >= nums[i+1]:
        i-=1
    if i>=0:
        j = len(nums) - 1
        while nums[i] >= nums[j]:
            j-=1
        nums[i],nums[j] = nums[j],nums[i]
    nums[i+1:] = reversed(nums[i+1:])
    return nums

nums = [1,2,3]
# nums = [3,2,1]
# nums = [1,1,5]
nextpermut(nums)
print(nums)