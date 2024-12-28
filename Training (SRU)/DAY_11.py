class Day11:
    
    def __init__(self,Binary,sorting):
        self.Binary = Binary
        self.sorting = sorting
    
    
    def linearsearch(self,target):
        
        for i in range(len(self.Binary)):
            if self.Binary[i] == target:
                return i
        return -1
    
    def bubblesort(self):

        for i in range(len(self.sorting)):
            for j in range(len(self.sorting) - i -1):
                if self.sorting[j] > self.sorting[j+1]:
                    self.sorting[j],self.sorting[j+1] = self.sorting[j+1],self.sorting[j]
        print(self.sorting)
        
    def insertionsort(self):
        
        for i in range(len(self.sorting)):
            
            key = self.sorting[i]
            j = i-1
            
            while j >= 0 and key < self.sorting[j]:
                self.sorting[j+1] = self.sorting[j]
                j-=1
            self.sorting[j+1] = key
        print(self.sorting)
    
    def selectionsort(self):
        for i in range(len(self.sorting)):
            mini = i
            for j in range(i+1,len(self.sorting)):
                if self.sorting[j] < self.sorting[mini]:
                    mini = j
            self.sorting[i],self.sorting[mini] = self.sorting[mini],self.sorting[i]
        print(self.sorting)
        
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [900,1,2,3,45,34,56,90,100,130]
arr = Day11(list1,list2)
# print(arr.linearsearch(10))
# arr.bubblesort()
# arr.insertionsort()
# arr.selectionsort()
