class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
    
def printing(head):
    print("forward:",end="")
    while head.next:
        print(head.data,end=" ")
        head = head.next
    print(head.data)
    print("backward:",end="")
    while head:
        print(head.data,end=" ")
        head = head.prev
        
def insert_begin(head,data):
    
        node = Node(data)
        if not head:
            return node
        head.prev = node
        node.next = head
        
        return node
    
def insert_end(self,data):
    node = Node(data)
    if not head:
        return node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    node.prev = curr
    return head
        
    
if __name__ == "__main__":
    head = None
    # list1 = [5,4,3,2,1]
    # for i in list1:
    #     head = insert_begin(head,i)
        
    list1 = [1,2,3,4,5]
    for i in list1:
        head = insert_end(head,i)
    printing(head)