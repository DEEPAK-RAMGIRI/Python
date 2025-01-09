# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def find_middle(head):
#     slow = head
#     fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow


# def display(head):
#     curr = head
#     while curr:
#         print(curr.data, end=" -> ")
#         curr = curr.next
#     print("NULL")

# n1 = Node(10)
# n2 = Node(20)
# n3 = Node(30)
# n4 = Node(40)
# n5 = Node(50)

# n1.next = n2
# n2.next = n3
# n3.next = n4
# n4.next = n5

# # print("Linked List:")
# # display(n1)

# # middle_node = find_middle(n1)
# # print(f"The middle element is: {middle_node.data if middle_node else 'No middle (empty list)'}")








# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def remove_nth_from_end(self, n):
#         dummy = Node(0)
#         dummy.next = self.head
#         slow = dummy
#         fast = dummy

#         for _ in range(n + 1):
#             if fast:
#                 fast = fast.next
#             else:
#                 return  

#         while fast:
#             slow = slow.next
#             fast = fast.next

#         slow.next = slow.next.next

#         self.head = dummy.next

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("NULL")


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node

#     def remove_duplicates(self):
#         if not self.head:
#             return
#         seen = set()
#         curr = self.head
#         prev = None
#         while curr:
#             if curr.data in seen:
#                 prev.next = curr.next
#             else:
#                 seen.add(curr.data)
#                 prev = curr
#             curr = curr.next

#     def display(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" ")
#             temp = temp.next
#         print()


# ll = LinkedList()
# ll.add(12)
# ll.add(13)
# ll.add(14)
# ll.add(12)
# ll.add(16)

# # print("Original Linked List:")
# # ll.display()

# # ll.remove_duplicates()

# # print("Linked List after removing duplicates:")
# # ll.display()


# #WAP ro check whether the given linked list is plaindrome or not

# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def palindrome_list(head):
#     values = []
#     temp = head
#     while temp:
#         values.append(temp.data)
#         temp = temp.next
#     if(values == values[::-1]):
#         print("\nis a palindrome")
#     else:
#         print("\nnot palindrome")

# def display(curr):
#     while(curr!=None):
#         print(curr.data,end=" -> ")
#         curr=curr.next
#     #print("NULL")

# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(20)
# n5=Node(10)

# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5

# curr=n1
# display(curr)

# head=n1
# curr=palindrome_list(head)
# display(curr)


# # Example usage:
# ll = LinkedList()
# for val in [1, 2, 3, 4, 5]:
#     ll.add(val)

# print("Original Linked List:")
# ll.display()

# n = 2
# ll.remove_nth_from_end(n)

# print(f"Linked List after removing the {n}th node from the end:")
# ll.display()

# '''
# 6. WAP to check if it has valid parenthesis
# '''
# def validParenthesis(str1):
#     s3=[] #stack
#     for i in str1:
#         if i in "({[":
#             s3.append(i)
#         else:
#             if len(s3)==0:
#                 return False
#             else:
#                 temp = s3.pop()
#                 if (temp == '(' and i != ')') or (temp == '[' and i != ']') or (temp == '{' and i != '}'):
#                     return False
            
#     return True


# class Node:
    
#     def __init__(self,data):
#         self.data=data
#         self.next=None

# def rev_list(head):
#     curr=head
#     prev=None
#     while curr!=None:
#         new_node=curr.next
#         curr.next=prev
#         prev=curr
#         curr=new_node
#     return prev

# def display(curr):
#     while(curr!=None):
#         print(curr.data,end=" -> ")
#         curr=curr.next
#     print("NULL")

# n1=Node(10)
# n2=Node(20)
# n3=Node(30)
# n4=Node(40)
# n5=Node(50)

# n1.next=n2
# n2.next=n3
# n3.next=n4
# n4.next=n5

# curr=n1
# display(curr)

# head=n1
# curr=rev_list(head)
# display(curr)


# print(validParenthesis("{[]}")) #True
# print(validParenthesis("([)]")) # False
# '''
# 7.WAP to find next greater element
# '''
# s=[] # stack
# s.append(12)
# s.append(15)
# s.append(26)
# s.append(19)
# s.append(2)
# def nextGreaterElement(s):
#     k=len(s)
#     max = s[0]
#     print(s)
#     for i in range(0,k):
#         for j in range(0,i):
#             if(max<s[j]):
#                 max=s[j]
#         print(max,end ="  ")

# nextGreaterElement(s)

# '''
# 8.WAP to evaluate postfix expression

# '''

# def evaluate_postfix(expression):
#     s4 = []
#     for i in expression:
#         if i.isdigit():
#             s4.append(int(i))
#         else:
#             operand2 = s4.pop()
#             operand1 = s4.pop()
#             if i == '+':
#                 s4.append(operand1 + operand2)
#             elif i == '-':
#                 s4.append(operand1 - operand2)
#             elif i == '*':
#                 s4.append(operand1 * operand2)
#             elif i == '/':
#                 s4.append(int(operand1 / operand2))
#     return s4[0]

# print(evaluate_postfix("231*+9-"))

# '''
# 9.WAP to sort a stack
# '''
# def func1(s):
#     n=len(s)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if s[j]>s[j+1]: 
#                 s[j], s[j + 1] = s[j + 1], s[j]
                
# func1(s)
# print(s)
# '''
# 10.WAP to reverse a string using stack 
# '''
# s1,s2=[],[]
# s1.append('s')
# s1.append('t')
# s1.append('a')
# s1.append('c')
# s1.append('k')
# print("Before:",s1)
# n=len(s1)
# for i in range(n-1,-1,-1):
#     s2.append(s1[i])
# print(s2)

# '''
# 11.WAP to generate n bianry numbers using queues
# '''

# def generate_binary_numbers(n):
#     q3 = ["1"]
#     res = []
#     for _ in range(n):
#         binary = q3.pop(0)
#         res.append(binary)
#         q3.append(binary + "0")
#         q3.append(binary + "1")
#     return res

# print(generate_binary_numbers(7))

# '''
# 12 WAP to reverse an queue
# '''
# q1,q2=[],[] #queue
# q1.append(1)
# q1.append(2)
# q1.append(3)
# q1.append(4)
# q1.append(5)
# n4=len(q1)
# for i in range(n4-1,-1,-1):
#     q2.append(q1[i])
# print(q2)

#print Binary value:
