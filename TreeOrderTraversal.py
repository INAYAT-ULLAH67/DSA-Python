
# from tree import Btree
from TreeNode import TreeNode
def preorder(node):
    if node is None:
        return
    print(node.value, end=' --->  ')      # Step 1: Visit root
    preorder(node.left)     # Step 2: Traverse left
    preorder(node.right)    # Step 3: Traverse right

A=TreeNode('A')
B=TreeNode('B')
C=TreeNode('C')
D=TreeNode('D')
E=TreeNode('E')
F=TreeNode('F')
G=TreeNode('G') 
A.left = B
A.right = C
B.left = D
B.right = E
C.left = F
C.right = G 
print("preorder traversal:")    
preorder(A) 
print()
def postorder(node):
    if node is None:
        return
    postorder(node.left)    # Step 1: Traverse left
    postorder(node.right)   # Step 2: Traverse right
    print(node.value, end=' --->  ')  # Step 3: Visit root
print("postorder traversal:")
postorder(A)
print()

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=' --->  ')  # Step 3: Vi
    inorder(node.right)
print("inorder traversal:")
inorder(A)
print()

