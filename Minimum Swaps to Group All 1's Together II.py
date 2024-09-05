def minSwaps(nums):
        total = sum(nums)  
        n = len(nums)
        if total == 0:
            return 0
        nums *= 2
        window_sum = sum(nums[:total])
        max_ones = window_sum
        swaps = total - max_ones
        for i in range(1, n):
            window_sum += nums[i + total - 1] - nums[i - 1]
            max_ones = max(max_ones, window_sum)
            swaps = min(swaps, total - max_ones)
        return swaps
a=[1,1,0,0,1]
print(minSwaps(a))