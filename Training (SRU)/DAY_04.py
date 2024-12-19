class Day04:
    def __init__(self,number,list1):
        self.number = number
        self.list1 = list1
        
    def max_in_digit(self,num1):
        num1 = map(int,list(num1))
        print(max(num1))
        
    def pattern1(self):
        print('\n'.join(i * '* ' for i in range(1,self.number+1)))
    
    def pattern2(self):
        #  print('\n'.join(i * '* ' for i in range(1,self.number+1))) 
        for i in range(1,self.number+1):
            print('*',end=' ')
         
    def Escape_seq_char(self):
        print("hello,\tit will print after a tab space\nit will be print in next line")
        
    # print a square
    def pattern3(self):
        
        # Method 1
        # for i in range(1,self.number+1):
        #     for j in range(1,self.number+1):
        #         print('*',end=' ')
        #     print()
        
        #    Method 02
        
        # for i in range(1,self.number+1):
        #     print('* ' * (self.number+1))
        
        # Method 03
        print('\n'.join(((self.number)) * '* ' for i in range(self.number)))
        
    def pattern4_patern1_reverse(self):
        #Method 1
        # for i in range(self.number):
        #     for _ in range(self.number- i):
        #         print("*",end=' ')
        #     print()
        
        #Method 2
        print('\n'.join('* ' * _ for _ in range(self.number,0,-1)))
        
    def pattern5_pyramid(self):
        for i in range(self.number):
            for _ in range(self.number-i-1):
                print(" ",end=' ')
            for _ in range(i*2+1):
                print("*",end=' ')
            print()
            
    def reverseString(self,string):
        # print(string[::-1])
        string = list(string)
        left = 0
        right = len(string)-1 
        while left < right :
            string[left],string[right] = string[right],string[left]
            left+=1
            right-=1
        print(''.join((string)))   
        
    # find max and min in the array
    def min_max_in_array(self):
        # print(f"maximum is:{max(self.list1)} and minimum is:{min(self.list1)}")
        maxs =float('-inf')
        mins =float('inf')
        
        for _ in self.list1:
            if _ >= maxs:
                maxs = _
            if _ <= mins:
                mins = _
        print(f"maximum is:{maxs} and minimum is:{mins}")
        
    def array_sort_or_not(self):
        for i in range(1,len(self.list1)-1):
            if self.list1[i] < self.list1[i-1]:
                print("Array is not sorted")
                return
        print("Array is sorted")
            
    def remove_duplicate_and_print(self):
        # new_array = []
        # for i in self.list1:
        #     if i not in new_array:
        #         new_array.append(i)
        # print(new_array)
        
        #method 02 
        print(list(set(self.list1)))
        
    # def 
                
                
        
number = 10 #int(input())    
list1 = [1,2,4,1,-1,56,12,234,2]
# list2 = [1,2,3,4,5,6]    
obj1 = Day04(number,list1)
# obj1.max_in_digit('9901')
# obj1.pattern1()
# obj1.pattern2()
# obj1.Escape_seq_char()
# obj1.pattern3()
# obj1.pattern4_patern1_reverse()
# obj1.pattern5_pyramid()

# string = 'god'
# obj1.reverseString(string)
# obj1.min_max_in_array()
# obj1.array_sort_or_not()

obj1.remove_duplicate_and_print()


