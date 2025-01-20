class Node:
    def __init__(self,data):
        self.data = data
        self.child = None
        self.next = None
        
def flatten(head):
    
    tail = head
    while tail.next:
        tail = tail.next
    
    curr = head
    while curr:
        if curr.child is not None:
            tail.next = curr.child
          
            while tail.next:
                tail = tail.next
          
            curr.child = None
            
        curr = curr.next
    return head

def printing(head):
    while head:
        print(head.data,end=" ")
        head = head.next


if __name__ == "__main__":
     #Linked List - 
    # 1 -> 2 -> 3
    # |         |   
    # 4 -> 5   6
    # |
    # 7
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.child = Node(4)
    head.child.next = Node(5)
    head.next.next.child = Node(6)
    head.child.child = Node(7)
    
    flatten(head)
    printing(head)
        