# import array as arr   # defined arr u haev to use like arr.array('i',[1,2,3,4])
import math
class Arrays:
    
    def __init__(self,array):
        self.a1 = array
        
        
    # MINIMUM AND MAXIMUM OF ARRAY
    def min_and_max(self):
        # Method 1 
        # print(f"Minimum is:{min(self.a1)}\nMaximum is:{max(self.a1)}")
        
    
        #method 02 dont use these this is just  for practice only
        # mini = min(i for i in self.a1)
        # print(f"mini = {mini}")
        # #method 03
        # maxi = max(i for i in self.a1)
        # print(f"maxi = {maxi}")
        
        
        # method 3
        maxi = float('-inf')
        mini = float('inf')
        
        for i in self.a1:
            if maxi < i:
                maxi = i
            if mini > i :
                mini = i
        print(f"maxi = {maxi}\nmini = {mini}")
        
        
    # REVERSE OF THE ARRAY
    
    def reverse_of_array(self):
        # print(f"Reverse of the Array: {self.a1[::-1]}")
        
        for i in range(len(self.a1)//2):
            self.a1[len(self.a1) - i - 1],self.a1[i] = self.a1[i],self.a1[len(self.a1)-i-1]
            
        print(f"Reverse of the Array: {self.a1}")
        
if __name__ == "__main__":
    array1 = [1,2,3,5,89,12,567,56,23,1]
    arr = Arrays(array1)
    # arr.min_and_max()
    arr.reverse_of_array()

    