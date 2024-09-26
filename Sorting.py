class arr:
    def __init__(self,array):
        self.array =array

    def bubble_sort(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j],self.array[j+1] = self.array[j+1],self.array[j]
        return self.array 

    def selection_sort(self):
        for i in range(len(self.array)):
            smallest = i
            for j in range(len(self.array)-1):
                if self.array[smallest] > self.array[j]:
                    smallest=j 
        self.array[i],self.array[smallest] =self.array[smallest],self.array[i]
        return self.array

    def insertion_sort(self):
        for i in range(1,len(self.array)):
            current = self.array[i]
            j =i-1
            while j>=0 and current < self.array[j]:
                self.array[j+1] = self.array[j]
                j-=1
            self.array[j+1] = current
        return self.array
    
    
    
    def partition(self,low,high):
        pivot = self.array[high]
        j=low-1
        for i in range(low,high):
            if pivot > self.array[i]:
                j+=1
                self.array[j],self.array[i] =self.array[i],self.array[j]
        self.array[j+1],self.array[high]=pivot,self.array[j+1]
        return j+1 
            
    
    def quick_sort(self,low,high):
        if low < high:
            pivot = self.partition(low,high)
            self.quick_sort(low,pivot-1)
            self.quick_sort(pivot+1,high)
        return self.array
        
            
        
if __name__ == "__main__":
    array = arr([1,343,0,112])
    #print(array.bubble_sort())
    #print(array.selection_sort())
    #print(array.insertion_sort())
    print(array.quick_sort(0,3))
                