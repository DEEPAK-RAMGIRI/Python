class Day05:
    
    def __init__(self,list1):
        self.list1 = list1
        
    def length(self):
        return len(self.list1)
    
    #finding count duplicate which is greater than n//2 
    def find_dup_in_list(self):
        n = self.length()
        for i in list1:
            return (i if self.list1.count(i) >= n//2 else 0)
        
    def rotate_left_array(self):
        n = int(input())
        # k=self.length()
        
        # while n >= (k-1):
        #     n -= k
        
        # ans =[]
        # ans.extend(self.list1[n:])
        # ans.extend(self.list1[:n])
        # print(ans)
        
        for _ in range(n):
            self.list1.append(self.list1.pop(0))
        
        print(self.list1)
    
    def longest_prefix(self,string):
        # count = 0
        # mini = float('inf')
        # for i in string:
        #     if len(i) < mini:
        #         mini = len(i)
        #         prefix = i
        # string.remove(prefix)
        # prefix = list(prefix)
        
        # for i in range(len(string)):
        #     first = list(string[i])
        #     for j in range(len(prefix)):
        #         if prefix[j] == first[j]:
        #             count+=1
        # print(''.join(prefix[:count//len(string)]) if count > 0 else "" )
       
       
       # better  use these one :)
       #time complexcirt is O(n*m) may be 
        prefix = string[0]
        for i in string:
            while prefix and prefix != i[:len(prefix)]:
                prefix = prefix[:-1]
        print(prefix)
                
        
            

list1 = [1,2,3,4,5,67,37]
# list1 = [1,1,1,2,3]
obj = Day05(list1)
# print(obj.find_dup_in_list())
# obj.rotate_left_array()
string_list =['flower','fly','flow','flight'] #list(input().split())
# string_list = ["dog","eat","in"]
obj.longest_prefix(string_list)

