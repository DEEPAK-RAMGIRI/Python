from collections import deque
class queues:
    def __init__(self):
        self.queue = deque()
        self.maxi = float('-inf')
        self.mini = float('inf')
        
    def enqueue(self,value):
        self.queue.append(value)
        self.maxi = max(self.maxi,value)
        self.mini = min(self.mini,value)
    
    def dequeue(self):
        if not self.queue:
            print("Queue is Empty")
            return None
        self.queue.popleft()
        self.maxi = max(self.queue)
        self.mini = min(self.queue)
        
    def find_max(self):
        print(self.maxi)
    
    def find_min(self):
        print(self.mini)
        
    def display(self):
        if not self.queue:
            print("false Queue is Empty")
            return None
        print(self.queue)
    
    def reverse(self):
        # if not self.queue:
        #     return None
        # print(list(self.queue)[::-1])
        n = len(self.queue)
        for i in range(n//2):
            self.queue[n-i-1],self.queue[i] = self.queue[i],self.queue[n-i-1]
            

        
        
queue = queues()

list1 = [10,2,2,0,4,5,5,2,2,1]
for i in list1:
    queue.enqueue(i)
# queue.find_max()
# queue.find_min()  
# queue.dequeue()
# queue.find_max()

# queue.reverse()
# queue.display()


class Binary:
    def __init__(self,no):
        self.no = no
        
    def print_Binary(self):
        print(bin(self.no)[2:])
    
    def normal_method(self):
        number = self.no
        value = ""
        while number >0:
            value=str(number%2) + value
            number//=2
        print(value)
no = Binary(15)
# no.print_Binary()
# no.normal_method()


#Spiral matrix
a = [[1, 2, 3, 4, 5, 6], 
     [18, 19, 20, 21, 22,7], 
     [17, 28, 29, 30, 23, 8],
     [16, 27, 26, 25, 24, 9], 
     [15, 14, 13, 12, 11, 10]]
rowstart = 0
colstart = 0
rowend = len(a)-1
colend = len(a[0])-1
ans =[]
while rowstart <= rowend and colstart <= colend:
    
    for col in range(colstart,colend+1):
        ans.append(a[rowstart][col])
    rowstart+=1
    
    for row in range(rowstart,rowend+1):
        ans.append(a[row][colend])
    colend-=1

    if rowstart <= rowend:
        for col in range(colend, colstart - 1, -1):
            ans.append(a[rowend][col])
        rowend -= 1
    
    if colstart <= colend:
        for row in range(rowend, rowstart - 1, -1):
            ans.append(a[row][colstart])
        colstart += 1
    
    
for  i,val in enumerate(ans,1): # here 1 means it start from 1 if not given it start from 0
    print(val,end=" ")
    if not i%len(a[0]):
        print()
    
