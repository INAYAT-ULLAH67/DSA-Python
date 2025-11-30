
# from tree import Btree
from TreeNode import TreeNode
def preorder(node):
    if node is None:
        return
    print(node.value, end=' --->  ')      # Step 1: Visit root
    preorder(node.left)     # Step 2: Traverse left
    preorder(node.right)    # Step 3: Traverse right

print()
def postorder(node):
    if node is None:
        return
    postorder(node.left)    # Step 1: Traverse left
    postorder(node.right)   # Step 2: Traverse right
    print(node.value, end=' --->  ')  # Step 3: Visit root
def depth_first_traversal(node):
    if node is None:
        return
        
    nodes = [node]   # nodes-like list
    print(node.value, end=' ---> ')
    
    i = 0  # index of current node ,visiting node
    n = 0  # index of last node in the list

    while i <= n:
        current_node = nodes[i]
        # print("\nVisiting Node:", current_node.value, ", and i and n:", i, n)

        if current_node.left is not None:
            nodes.append(current_node.left)
            n += 1
            print(current_node.left.value, end=' ---> ')

        if current_node.right is not None:
            nodes.append(current_node.right)
            n += 1
            print(current_node.right.value, end=' ---> ')

        i += 1
        



def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end=' --->  ')  # Step 3: Vi
    inorder(node.right)



# Helper function to build a tree from a list
# Using level order insertion
def buildTree(val):
    if not val or val[0] == -1:
        return None

    root = TreeNode(val[0])
    nodes = [root]
    i = 1
    n = 0

    while i < len(val):
        currentNode = nodes[n]

        # LEFT CHILD
        if val[i] is not None:
            left = currentNode.addLeftChild(val[i])
            nodes.append(left)
        i += 1

        # RIGHT CHILD
        if i < len(val) and val[i] is not None:
            right = currentNode.addRightChild(val[i])
            nodes.append(right)
        i += 1

        n += 1

    return root

# Example usage:
# Creating the following
# binary tree:
#         A
#       /   \
#      B     C
#     / \   / \
#    D   E F   G
#       /       \
#      H         I
butree=buildTree(['A', 'B', 'C', 'D', 'E', 'F', 'G', None, None, 'H', None, None, None, 'I'])
print("Preorder Traversal of built tree:")
preorder(butree)
print("\nInorder Traversal of built tree:")
inorder(butree)
print("\nPostorder Traversal of built tree:")
postorder(butree)
print()     
A=TreeNode('A')
#         A
#       /   \
#      B     C
#     / \   / 
#    D   E F 
#       /   \
#      H     G
#             \
#              I
A=TreeNode('A')
B=TreeNode('B')
C=TreeNode('C')
D=TreeNode('D')
E=TreeNode('E')
F=TreeNode('F')
G=TreeNode('G')
H=TreeNode('H')
I=TreeNode('I') 
A.left=B
A.right=C
B.left=D
B.right=E
E.left=H
C.left=F
F.right=G
G.right=I   

print("Preorder Traversal:")
preorder(A)
print("\nPostorder Traversal:")
postorder(A)
print()
print("\nInorder Traversal:")
inorder(A)
print
print("\nDepth-First Traversal:")
depth_first_traversal(A)
print()
# A binary tree node