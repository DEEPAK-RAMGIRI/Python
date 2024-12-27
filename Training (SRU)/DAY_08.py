class Day08:
    def __init__(self,function1):
        self.list1 = function1
        
    def diff_minmax_in_subarray(self):
        n =len(self.list1)
        sums = 0
        for i in range(n):
            for j in range(i+1,n+1):
                mini,maxi = min(self.list1[i:j]),max(self.list1[i:j])
                sums += maxi-mini
        print(sums) 
    
    def nth_largest_and_smallest(self,n):
        self.list1.sort()
        print(f"{n}th largest is : {self.list1[-n]} and {n}th mini is:{self.list1[n-1]}")
        
                
                
                
list1 = [2,1,3]
obj = Day08(list1)
# obj.diff_minmax_in_subarray()
# obj.nth_largest_and_smallest(2)



class Stack:
    def __init__(self):
        self.stack = []
        
    def add(self,data):
        return self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def length(self):
        print(f"length of stack is: {len(self.stack)}")
    
    def printing(self):
        print(self.stack)
        
stack =Stack()
stack.add(10)
stack.add(20)
stack.add(30)
# stack.printing()
# stack.pop()
# stack.length()


class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
        # self.prev=None
        
def insert_first(head,node):
    if head is None:
        return node
    else:
        node.next = head
    return node

def insert_end(head,node):
    
    if head is None:
        return node
    
    curr = head
    
    while curr.next:
        curr=curr.next
    curr.next = node
    
    return head
    
def print_node(head):
    while head:
        print(head.data,"->",end=' ')
        head= head.next

def remove_head(head):
    
    if head is None:
        return None
    
    temp = head.data
    del temp
    head = head.next
    return head

def remove_last_ele(head):
    
    if head is None:
        return None
    
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None
    return head

               
def remove_ele(head,value):
    while head.next and head.data == value:
        head = head.next
        pass
    

        
if __name__ == "__main__":
    head = None
    list1 = [1,3,4,90,12,4342]
    
    for i in list1: 
        head = insert_first(head,Node(i))
        
    head = insert_end(head,Node(200))  
    head = remove_head(head)
    head = remove_last_ele(head)
    
    print_node(head)

