class Linkedlist:
    def __init__(self,data):
        self.data =  data
        self.next = None
        
def insert_end(head,data):
    node = Linkedlist(data)
    if head is None:
        return node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node
    return head

def printing(head):
    while head:
        print(head.data,end=" ")
        head = head.next
        
def delete_without_headnode(head):
    
    if head is None and head.next is None:
        return 
    
    curr = head.next
    print(head.data,"is deleted")
    del head
    return curr
    
def remove_dupliactes(head):
    curr1 = head
    while curr1:
        curr2 = curr1
        while curr2.next:
            if curr1.data == curr2.next.data:
                curr2.next = curr2.next.next
            else:
                curr2 = curr2.next
        curr1 = curr1.next
    return head

def remove_duplicates_hash_set(head):
    elements = set()
    curr = head
    prev= None
    while curr:
        if curr.data in elements:
            prev.next = curr.next
        else:
            elements.add(curr.data)
            prev = curr
        curr = curr.next
    return head

def sorting_0_1_2(head):
    curr = head
    count = [0]*3
    
    while curr:
        count[curr.data]+=1
        curr = curr.next
    index = 0 
        
    # temp = Linkedlist(0)
    # new_head = temp
    # for i in count:
    #     for _ in range(i):
    #         new_head.next = Linkedlist(index) 
    #         new_head = new_head.next
    #     index+=1
    # return temp.next
    
    #method 02
    
    curr = head
    while curr:
        if count[index] == 0:
            index+=1
        else:
            curr.data = index
            count[index] -= 1
            curr = curr.next
    return head

def multiply_two_linked_list(head1,head2):
    
    num1 = num2 = 0
    while head1:
        num1 = ((num1*10) + head1.data)
        head1 = head1.next
        
    while head2:
        num2 = ((num2*10) + head2.data)
        head2 = head2.next
        
    return num1*num2
        
def  remove_last_nth_node(head,value):
    
    fast,slow = head,head
    
    for _ in range(value):
        fast = fast.next
    if not fast:
        return  head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head

        

if __name__ == "__main__":
    
    # head = None
    
    # list1 = [1,2,3,4,5,6,7,8]
    # for i in list1:
    #     head = insert_end(head,i)
    # head = delete_without_headnode(head) 
    # printing(head)
    
    # head = None
    # list1 = [1,2,2,2,4,5,66,6,6,6,7,8,9]
    # for i in list1:
    #     head = insert_end(head,i)
    # head = remove_dupliactes(head)
    # printing(head)
    
    # head = None
    # list1 = [1,2,2,2,4,5,66,6,6,6,7,8,9]
    # for i in list1:
    #     head = insert_end(head,i)
    # head = remove_duplicates_hash_set(head)
    # printing(head)
    
    # head = None
    # list1 = [0,1,2,0,1,2,0,2]
    # for i in list1:
    #     head = insert_end(head,i)
    # head = sorting_0_1_2(head)
    # printing(head)
    
    # #muktiply two linked list
    # head1 = head2 = None
    # list1 = [5,5,5]
    # list2 = [1,0,0]
    
    # for i,j in zip(list1,list2):
    #     head1 = insert_end(head1,i)
    #     head2 = insert_end(head2,j)
    
    # print(multiply_two_linked_list(head1,head2))
    
    
    head = None
    list1 = [1,2,3,4,5,5,66,7]
    # list1 = [1]
    
    for i in list1:
        head = insert_end(head,i)
    value = 3
    head = remove_last_nth_node(head,value)  
    printing(head)
            