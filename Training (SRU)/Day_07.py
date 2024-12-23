class Day07:
    def __init__(self,nums,nums2):
        self.nums = nums
        self.nums2 = nums2
        
    def linear_search(self,target):
        # for i in self.nums:
        #     if i is target:
        #         return self.nums.index(i)
        # return -1
        
    # (or) we can say
        try:
            return self.nums.index(target)
        except ValueError:
            return -1
        
    
    def count_numbers(self,no):
        
        count = 0
        count_0 = no.count(0)
        for i in no:
            if i != 0:
                count+=1
        print(count + count_0//2 + count_0%2)
        
        # s=input()
        # print(len(s)-s.count('00'))
            
    def consecutive_Binarynums(self):
        count = 0
        maxs = 0 
        for i in nums:
            if i == 1:
                count +=1 
            else:
                if maxs > count:
                    maxs = count
                count = 0         
    def max_min_in_array(self):
        # print(f"Maximum is:{max(self.nums)} ,Minimum is: {min(self.nums)}")
        #(or) Method 02
        maxs = float('-inf')
        mins = float("inf")
        for i in self.nums:
            if maxs < i:
                maxs = i
            if mins > i:
                mins = i
        print(f"Maximum is:{maxs} ,Minimum is: {mins}") 
    
    
    def array_sorted(self):
        # return True if (sorted(self.nums) == self.nums) else False
        
        #method 02
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return False
        return True
                
    def secound_max_element(self):
        
        # maxi = max(self.nums)
        # while maxi in self.nums:
        #     self.nums.remove(maxi) # remove() takes O(n)
        # print(max(self.nums))
        
        maxs =secound= -1
        for i in self.nums:
            if i > maxs:
                secound =maxs
                maxs = i
            elif secound < i and i != maxs:
                secound = i
        print(secound if secound != -1 else None)
            
    def bubble_Sort(self,nums):
        length = len(nums)
        
        for i in range(length-1):
            for j in range(length-1-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
        
                     
    def Union_of_lists(self):
        nums3 = []
        
        # for i in self.nums:
        #     if i not in nums3:
        #         nums3.append(i)
                
        # for i in self.nums:
        #     if i not in nums3:
        #         flag = True
        #         for j in range(len(nums3)):
        #             if i < nums3[j]:
        #                 nums3.insert(j,i)
        #                 flag = False
        #                 break
        #         if flag:
        #             nums3.append(j)
                    
        # print(nums3)
        
        # or method 02
        
        # n1 = len(self.nums)
        # n2 = len(self.nums2)
        # left = right = 0
        # while left <n1 and right < n2:
        #     if self.nums[left] ==  self.nums2[right]:
        #         nums3.append(self.nums[left])
        #         left+=1
        #         right+=1
        #     elif self.nums[left] < self.nums2[right]:
        #         nums3.append(self.nums[left])
        #         left+=1
        #     else:
        #         if self.nums2[right] not in nums3:
        #             nums3.append(self.nums2[right])
        #         right+=1
        # while left < n1:
        #     if self.nums[left] not in nums3:
        #         nums3.append(self.nums[left])
        #     left+=1
        # while right < n2:
        #     if self.nums2[right] not in nums3:
        #         nums3.append(self.nums2[right])
        #     right+=1
            
        # print(nums3) 
        
        #method 03
        self.nums.extend(self.nums2)

        ans = (list(set(self.nums)))
        self.bubble_Sort(ans)
        print(ans)
    
    def majortity_ele(self):
        nums = [1,2, 1, 1,3,2,1]
        ans =[]
        for i in nums:
            if len(nums)//3 < nums.count(i) and i not in ans:
                ans.append(i)
        print(ans)
    
    
    def nth_largest_and_nth_smallest(self):
        pass
        
                    

        
nums = [1,2,3,4,10,34]
nums2 = [1,2,4,5,6,11]
# nums = [0,0,1,1,1,0,0,1]
obj = Day07(nums,nums2)
# print(obj.linear_search(10))
# obj.count_numbers([1,0,0,0])
# obj.max_min_in_array()
# print(obj.array_sorted())
# obj.secound_max_element()
# obj.Union_of_lists()
# obj.majortity_ele()


## LINKED LIST

    class Node:
        def __init__(self,data,next =None):
            self.data = data
            self.next = None
            
        def inserting_to_node(self):
            pass
        
        def printing(self):
            while self is not None:
                print(self.data)
                self = self.next
                
    node1 =Node(10)
    node2 =Node(20)
    node3 =Node(30)
    node4 =Node(40)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node1.printing()

