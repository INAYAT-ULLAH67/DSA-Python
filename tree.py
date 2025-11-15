from TreeNode import TreeNode

def preorder(node):
    if node is None:
        return
    print(node.value)       # Step 1: Visit root
    preorder(node.left)     # Step 2: Traverse left
    preorder(node.right)    # Step 3: Traverse right


#            9
#       6          8
# 3          1  4      2
A=TreeNode(9)
B=TreeNode(6)
C=TreeNode(8)
D=TreeNode(3)
E=TreeNode(1)
F=TreeNode(4)
G=TreeNode(2)
A.left=B
A.right=C
B.left=D
B.right=E
C.left=F
C.right=G
def preorder(node):
    if node is None:
        return
    print(node.value, end=' --->  ')      # Step 1: Visit root
    preorder(node.left)     # Step 2: Traverse left
    preorder(node.right)    # Step 3: Traverse right

preorder(A)
print()
def postorder(node):
    if node is None:
        return
    postorder(node.left)    # Step 1: Traverse left
    postorder(node.right)   # Step 2: Traverse right
    print(node.value, end=' --->  ')  # Step 3: Visit root

postorder(A)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value)
    inorder(node.right)