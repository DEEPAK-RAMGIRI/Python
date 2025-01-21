# Delete nodes which have a greater value on right side
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
       
        
def insert_end(head,data):
    
    node = Node(data)
    if not head:
        return node
    curr =head
    while curr.next:
        curr =curr.next 
    curr.next = node
    return head

def deletenode(head):
    
    #reverseing 
    prev,curr = None,head
    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
        
    temp = prev
    maxnode = prev    
    
    while temp and temp.next:
        if maxnode.data > temp.next.data:
            temp.next = temp.next.next
        else:
            temp = temp.next
            maxnode = temp
            
    prev,curr = None,prev
    while curr:
        nextnode = curr.next
        curr.next = prev
        prev = curr
        curr = nextnode
    return prev

def deletenode2(node):
    if not node or not node.next:
        return node
    nextnode = deletenode2(node.next)
    
    if nextnode.data > node.data:
        return nextnode
    
    node.next =nextnode
    return node
        

def printing(head):
    while head:
        print(head.data,end=" ")
        head = head.next
            
if __name__ == "__main__":
    # 12->15->10->11->5->6->2->3
    list1 = [12,15,10,11,5,6,2,3]
    head = None
    for i in list1:
        head = insert_end(head,i)
        
    # printing(deletenode(head))  
    printing(deletenode2(head))