# Segregate even and odd nodes in a Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert(head,data):
    node = Node(data)
    if not head:
        return node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    return head 

def evenoddseq(head):
    even = None
    odd = None
    
    while head:
        if head.data & 1:
            odd = insert(odd,head.data)
        else:
            even = insert(even,head.data)
        head = head.next
            
    curr = even
    
    while curr.next:
        curr = curr.next
    curr.next = odd
    return even
            
def printing(head):
    while head:
        print(head.data,end=" ")
        head = head.next
if __name__ == "__main__":
    #  17->15->8->12->10->5->4->1->7->6->NULL
    # 0->1->4->6->9->10->11
    # list1 = [0,1,4,6,9,10,11]
    # head = None
    # for i in list1:
    #     head = insert(head,i)
    # head = evenoddseq(head)
    # printing(head)
    list1 = [ 17,15,8,12,10,5,4,1,7,6]
    head = None
    for i in list1:
        head = insert(head,i)
    head = evenoddseq(head)
    printing(head)
    