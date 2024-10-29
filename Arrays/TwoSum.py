class Solution:
    def  __init__(self,nums):
        self.nums = nums;
        
    def twoSum(self,target):
        box = {}

        for i,n in enumerate(self.nums):
            
            diff = target - n
            if diff in box:
                return [box[diff],i]

            box[n] =i
        return []

if  __name__ == "__main__":
    obj1 = Solution([-1,-2,-3,-4,-5])
    print(obj1.twoSum(-8));

        