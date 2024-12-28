class Day10:
    pass
# Traversal Of Tree
'''
=> we have three types of traversal
  1. Preorder
  2. Inorder
  3. Postorder

1. Preorder Traversal:
=> Preorder traversal is a type of depth first search(DFs) where every node will be visited in the following order
=> In preorder traversal first it will visit root node then recursively it will do preorder traversal of left sub-tree 
   followed by preorder traversal by right sub-tree
   
=>                  1
                  /   \
                 2     3
                / \   / \
               4   5 6   7
        Traversal: 1->2->4->5->3->6->7    

Note:
=> for pre-traversal we have two different methods which are 
   1. Breadth-first search(BFs)
   2. Depth first search(DFs)
   
1. BFs:
=> In BFs the nodes on same level are visited before going to next level in the tree by using this method  
   we traverse in side wise direction

2. DFs:
=>In DFs the traversal will be  done in downward direction where traversal starts from root node to leaf node. 


2. Inorder Traversal:
=> Inorder traversal is a type of depth first search(DFs) 

=>                  1
                  /   \
                 2     3
                / \   / \
               4   5 6   7
                        /
                       8 
        Traversal: 4->2->5->1->6->3->8->7
        
3. PostOrder Traversal:
=> Postorder Traversal also belongs to depth first search(DFs) where each node will be visited in this following order

=>                  1
                  /   \
                 2     3
                / \   / \
               4   5 6   7
                        /
                       8 
            Traversal: 4->5->2->6->8->7->3->1
                  
=> Declare a function with name of preorder,inorder,postorder traversal
'''

class BinaryTree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def search(node,target):
    if node is None:
        return False
    if node.data == target:
        return True
    elif node.data < target:
        return search(node.right,target)
    else :
        return search(node.left,target)
    
def height_of_tree(node):
    if node is None:
        return False
    else:
        left = height_of_tree(node.left)
        right = height_of_tree(node.right)
    return 1+ max(left,right)

def sum_of_nodes(node):
    if node is None:
        return 0
    else:
        left = sum_of_nodes(node.left)
        right = sum_of_nodes(node.right)
    return node.data + left+ right
    
           
root=BinaryTree(10)
n1=BinaryTree(8)
n2=BinaryTree(7)
n3=BinaryTree(9)
n4=BinaryTree(11)
n5=BinaryTree(13)
n6=BinaryTree(12)
n7=BinaryTree(6)

root.left=n1
n1.left=n2
n1.right=n3
root.right=n4
n4.right=n6
n4.left=n5
n6.left = n7

# print(root.data)
# print(root.left.data,root.right.data)
# print(root.left.left.data,root.left.right.data)
print("Found" if search(root,12) else "Not Found")

# print(height_of_tree(root))

print(sum_of_nodes(root))

# print('Pre order traversal')
# 
def preorder(node):
    if node is None:
        return
    print(node.data,end=' ')
    preorder(node.left)
    preorder(node.right)
# preorder(root)

# print('\nInorder traversal')
def inorderTraversal(node):
    if node is None:
        return
    inorderTraversal(node.left)
    print(node.data,end=" ")
    inorderTraversal(node.right)
# inorderTraversal(root)

# print('\nPost order traversal')
def postorderTraversal(node):
    if node is None:
        return
    postorderTraversal(node.left)
    postorderTraversal(node.right)
    print(node.data,end=' ')
# postorderTraversal(root)