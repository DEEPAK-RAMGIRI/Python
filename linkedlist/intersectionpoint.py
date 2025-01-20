class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
# def insert(head,data):
#     new = node(data)
#     if head is None:
#         return new
#     curr = head
#     while curr.next:
#         curr = curr.next
#     curr.next = new
#     return head

def printing(head):
    if head is None:
        print("empty")
        return
    while head:
        print(head.data,end=" ")
        head = head.next
        
def intersectPoint(head1,head2):
    while head1:
        temp = head2
        while temp:
            if temp == head1:
                print(temp.data)
                return
            temp = temp.next
        head1 = head1.next
            
        
        
if __name__ == "__main__":  
          
        head1 = Node(10)
        head1.next = Node(15)
        head1.next.next = Node(30)

     
        head2 = Node(3)
        head2.next = Node(6)
        head2.next.next = Node(9)

   
        head2.next.next.next = head1.next
        
        # printing(head1)
        # printing(head2)
        intersectPoint(head1, head2)

