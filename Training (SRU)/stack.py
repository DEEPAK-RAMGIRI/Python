#stack sing linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
        
# class Stack:
    
#     def __init__(self,maxsize = 0):
#         self.stack = None
#         self.size = 0
#         self.maxS ize = maxsize
    
#     def push(self,data):
#         node = Node(data)
#         if self.size >= self.maxSize:
#             print("Stack is overflowing")
#             return None
#         elif not self.stack:
#             self.stack = node
#         else:    
#         # if self.stack.size <= maxSize:
#             curr = self.stack
#             while curr.next:
#                 curr = curr.next
#             curr.next = node
#         self.size+=1
        
#     def pop(self):
#         if not self.stack:
#             print("stack is empty")
#             self.stack = None
#         elif self.stack.next is None:
#             print("Stack is empty")
#             self.stack = None
#         else:
#             curr = self.stack
#             while curr.next.next:
#                 curr = curr.next
#             curr.next = None
#         self.size -=1
            
#     def top(self):
#         print(self.size)
#         curr = self.stack
#         while curr.next:
#             curr  = curr.next
#         print(curr.data)
#     def printing(self):
#         while self.stack:
#             print(self.stack.data,end = " ")
#             self.stack = self.stack.next    
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.pop()
# stack.pop()
# stack.top()
# stack.top()
# stack.printing()




class Stack:
    def __init__(self,maxsize=10):
        self.stack = []
        self.maxsize = maxsize
        self.top = -1
        
    def push(self,element):
        if self.top ==  self.maxsize - 1:
            print("Stack is overflowing")
            return 
        self.stack.append(element)
        self.top+=1
        
    def pop(self):
        if not self.stack:
            print("Stack is empty")
            return
        self.top -= 1
        return self.stack.pop()
    
    def peek(self):
        print(self.stack[self.top])
    def printing(self):
        print(self.stack)
        
        
    def isEmpty(self):
        return self.top == -1
        
        
if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.printing()
    stack.push(stack.pop() + stack.pop())
    stack.printing()

                
