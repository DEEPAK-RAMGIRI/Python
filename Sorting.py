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
            for j in range(i+1,len(self.array)):
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
    
    def conquer(self,start,end,mid):
        index1= start
        index2= mid+1
        merge =[0]*end-start+1
        ind=0
        while index1 <=mid and index2<=end:
            if self.array[index1] < self.array[index2]:
                merge[ind] = self.array[index1]
                index1+=1
            else:
                merge[ind] = self.array[index2]
                index2+=1
            ind+=1
        while index1 <= mid:
            merge[ind] = self.array[index1]
            ind+=1
            index1+=1
        while index2 <= end:
            merge[ind] = self.array[index2] 
            ind+=1
            index2+=1
        for i in range(len(merge)):
            self.array[start+i] = merge[i]
                        
                
        
        
    def merge_sort(self,start,end):
        if start < end:
            mid = (start +(end-start))//2
            self.merge_sort(start,mid)   
            self.merge_sort(mid+1,end)
            self.conquer(start,end,mid)                 
        
if __name__ == "__main__":
    array = arr([1,343,0,112])
    #print(array.bubble_sort())
    #print(array.selection_sort())
    #print(array.insertion_sort())
    # print(array.quick_sort(0,3))
    print(array.merge_sort(0,3))
                