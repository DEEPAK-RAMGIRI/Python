class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None


    def insert_begin(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return  
        node.next = self.head  
        self.head = node
        
    def insert_end(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = node
        
    def insert_middle(self,data):
        node = Node(data)
        slow = self.head
        speed = self.head
        while  speed and speed.next:
            slow = slow.next
            speed = speed.next.next
        node.next = slow.next
        slow.next = node
    
    def reverse_linked_list(self):
        curr = self.head
        prev = None
        while curr:
            next_node =  curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head  = prev
               
    def printing(self,string):
        print(f"\n{string}:")
        temp =self.head
        while temp:
            print(temp.data,end=" ")
            temp = temp.next
            
def prints_circle(start):
    slow = start
    speed = start
    print(slow.data,end=" ")
    while speed and speed.next:
        slow = slow.next
        speed = speed.next.next
        print(slow.data,end=" ")
        if speed == slow:
            break
        
def merge_linked_sorted(head1,head2):
    
    temp = Node(-1)
    new = temp
    
    while head1 and head2:
        if head1.data <= head2.data:
            new.next = head1
            head1 = head1.next
        else:
            new.next = head2
            head2 = head2.next
        new = new.next
    new.next = head1 if head1 else head2
    return temp.next
                      
if __name__ == "__main__":
    
    ll =Linkedlist()
    ll.insert_begin(120)
    ll.insert_begin(110)
    ll.insert_begin(100)
    ll.insert_end(130)
    ll.insert_end(140)
    ll.insert_middle(125)
    # ll.printing("normal")
    # ll.reverse_linked_list()
    
    ll2 = Linkedlist()
    ll2.insert_end(121)
    ll2.insert_end(340)
    ll2.insert_end(900)
    ll2.insert_end(1900)
    
    # ll.printing("reversed")
    
    # n1 = Node(100)
    # n2 = Node(110)
    # n3 = Node(115)
    # n4 = Node(120)
    # n5 = Node(130)
    # n6 = Node(140)
    # n1.next = n2
    # n2.next = n3
    # n3.next = n4
    # n4.next = n5
    # n5.next = n6
    # n6.next = n2

    temp = merge_linked_sorted(ll.head,ll2.head)
    
    while temp:
        print(temp.data , end = " ")
        temp = temp.next
    