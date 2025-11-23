from TreeNode import TreeNode

class Btree:
    def __init__(self):
        self.root = None

    def addRoot(self, item):
        if self.root is None:
            self.root = TreeNode(item)
        else:
            print("Root already exists")

    def addLeftChild(self, item):
        if self.root is None:
            print("Root is empty, add a root first")
        elif self.root.left is None:
            self.root.left = TreeNode(item)
            return self.root.left
        else:
            print("Left node is already present")
            return self.root.left

    def addRightChild(self, item):
        if self.root is None:
            print("Root is empty, add a root first")
        elif self.root.right is None:
            self.root.right = TreeNode(item)
            return self.root.right
        else:
            print("Right node is already present")
            return self.root.right

    def DelLeftChild(self):
        if self.root is None:
            print("Tree is empty")
        elif self.root.left is None:
            print("Left child is not present!")
        elif self.root.left.left is None and self.root.left.right is None:
            x = self.root.left.value
            self.root.left = None
            print(f"Deleted left child with value {x}")
            return x
        else:
            print("Left child has its own children, cannot delete directly")

    def DelRightChild(self):
        if self.root is None:
            print("Tree is empty")
        elif self.root.right is None:
            print("Right child is not present!")
        elif self.root.right.left is None and self.root.right.right is None:
            x = self.root.right.value
            self.root.right = None
            print(f"Deleted right child with value {x}")
            return x
        else:
            print("Right child has its own children, cannot delete directly")
    def height(self):
        if self.left is None and self.right is None:
            return 1   # leaf node has height 1
        rh=0
        lh=0
        if self.right is not None:
            rh=self.right.height()

        if self.left is not None:
            lh=self.left.height()
        if rh>lh:
            return rh+1
        return lh+1

    def nodeCount(self):
        if self.left is None and self.right is None:
            return 1   # leaf node counts as 1
        lnc=0
        rnc=0
        if self.left is not None:
            lnc=self.left.nodeCount()
        if self.right is not None:
            rnc=self.right.nodeCount()
        return lnc + rnc + 1
    
    def leafCout(self):
        if self.left is None and self.right is None:
            return 1   # leaf node counts as 1
        lfc=0
        rfc=0
        if self.left is not None:
            lfc=self.left.leafCout()
        if self.right is not None:
            rfc=self.right.leafCout()
        return lfc + rfc

        

bt = Btree()
bt.addRoot(10)
left1 = bt.addLeftChild(5)
right1 = bt.addRightChild(15)

# You can now attach children to left1 or right1
left1.left = TreeNode(2)
left1.right = TreeNode(7)

print("Root:", bt.root)          # 10
print("Left:", bt.root.left)     # 5
print("Right:", bt.root.right)   # 15
print("Left->Left:", left1.left) # 2
print("Left->Right:", left1.right) # 7













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


