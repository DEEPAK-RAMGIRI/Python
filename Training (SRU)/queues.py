# class Queue:
#     def __init__(self,capacity):
#         self.front = 0
#         self.rear = -1
#         self.capacity =capacity
#         self.que = [None]*capacity
    
#     def enqueue(self,value):
#         if self.rear == self.capacity - 1:
#             print("queue is full")
#             return
#         self.rear+=1
#         self.que[self.rear] = value

#     def dequeue(self):
#         if self.front > self.rear:
#             print("Queue is empty")
#             return
#         value = self.que[self.front]
#         self.front+=1
#         return value
         

        
# if __name__ == "__main__":
#     nos = [1,2,3,5,6,7,10,8,9,9]
#     queue = Queue(10)    
#     for i in nos:
#         queue.enqueue(i)
    
#     while queue.front <= queue.rear:
#         print(queue.dequeue(), end=" ")   



# Direct import of queue
# from queue import Queue
# q = Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# print(q.get())
# while not q.empty():
#     print(q.get())
 
 
 
 
 #using linked list
# class Node:
#      def __init__(self,data):
#          self.data = data
#          self.next = None
# class Queue:
#     def __init__(self):
#         self.front = None
#         self.rear = None
#     def enqueue(self,data):
#         que = Node(data)
#         if not self.rear:
#             self.front = self.rear = que
#             return
#         self.rear.next = que
#         self.rear = que
#     def dequeue(self):
#         if self.isempty():
#             return
#         elif self.front == self.rear:
#             self.rear = self.front = None
#             return 
#         else:
#             value = self.front.data
#             self.front = self.front.next
#             return value
        
#     def isempty(self):
#         return self.front is None
        
# q = Queue()
# list1 = [1,2,3,4,5,6]
# for i in list1:
#     q.enqueue(i)
    
# while not q.isempty():
#     print(q.dequeue())

            
            
            
# # deque means double ended queue
# from collections import deque
# d = deque()
# d.append("hello")
# d.append("world")
# d.appendleft("it's me")
# print(d)
# d.pop()
# print(d)
# d.popleft()
# print(d) 



# double ended queue using linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class Dqueue:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def append(self,value):
        node = Node(value)
        if not self.rear:
            self.front = self.rear = node
            return
        self.rear.next = node
        node.prev = self.rear
        self.rear = node
        
    def pop(self):
        if self.isempty():
            return None
        elif self.front is self.rear:
            value = self.rear.data
            self.front = self.rear = None
            return value
        else:
            value = self.rear.data
            self.rear =self.rear.prev
            return value
    
    def isempty(self):
        return self.front == None
    def appendleft(self,value):
        node = Node(value)
        if self.isempty():
            self.front = self.rear = node
            return
        node.next =self.front
        self.front.prev = node
        self.front = node
    def popleft(self):
        if self.isempty():
            return
        elif self.front is self.rear:
            value = self.front.data
            self.front = self.rear = None
            return value
        else:
            value = self.front.data
            self.front = self.front.next
            self.front.prev = None
            return value
        
    def printing(self):
        temp = self.front
        while temp.next:
            print(temp.data,end=" ")
            temp = temp.next

        print(temp.data)
        while temp:
            print(temp.data,end=" ")
            temp = temp.prev
    
        
list1 = [1,2,3,4,5,6,7,8,9,10]
dequ = Dqueue()
for i in list1:
    dequ.appendleft(i)
# while not dequ.isempty():
#     print(dequ.popleft())
dequ.printing()
    