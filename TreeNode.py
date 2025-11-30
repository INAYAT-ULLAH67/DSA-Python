class TreeNode:
    def __init__(self, value):
        self.left = None
        self.value = value
        self.right = None

    def height(self):
        if self.left is None and self.right is None:
            return 1  # leaf node has height 1
        rh = 0
        lh = 0
        if self.right is not None:
            rh = self.right.height()
        if self.left is not None:
            lh = self.left.height()
        if rh > lh:
            return rh + 1
        return lh + 1

    def nodeCount(self):
        if self.left is None and self.right is None:
            return 1  # leaf node counts as 1
        lnc = 0
        rnc = 0
        if self.left is not None:
            lnc = self.left.nodeCount()
        if self.right is not None:
            rnc = self.right.nodeCount()
        return lnc + rnc + 1

    def leafCount(self):
        if self.left is None and self.right is None:
            return 1  # leaf node counts as 1
        lfc = 0
        rfc = 0
        if self.left is not None:
            lfc = self.left.leafCount()
        if self.right is not None:
            rfc = self.right.leafCount()
        return lfc + rfc

    def addLeftChild(self, item):
        if self.left is None:
            self.left = TreeNode(item)
            return self.left
        else:
            print("Left child already present")
            return self.left

    def addRightChild(self, item):
        if self.right is None:
            self.right = TreeNode(item)
            return self.right
        else:
            print("Right child already present")
            return self.right
    def depth(self):
        d = 0
        node = self
        while node:
            d += 1
            node = node.left
        return d
    def isperfect(self):
        d = self.depth()
        return self._isPerfectRecur(self, d)

    def _isPerfectRecur(self, node, d, level=0):
        if node is None:
            return d == level
        if node.left is None and node.right is None:
            return d == level + 1
        if node.left is None or node.right is None:
            return False
        return (self._isPerfectRecur(node.left, d, level + 1) and
                self._isPerfectRecur(node.right, d, level + 1))

    def almostCompleteBtrre(self):
        if self.isperfect():
            return True

        if self.left is None:
            return False
            # we have two nodes one is root and another is
            # right child .
        heightLeft = self.left.height()

        if self.right is None:
            if heightLeft==1:
                return True
                # if there is no right child and height of right 
                # sub tree is 0
            return False
        # right sub tree height
        height_right=self.right.height()
        # if height of left sub tree is equal to height of right sub tree
        # then left sub tree must be perfect and right sub tree must be
        # almost complete binary tree
        if heightLeft==height_right:
            return self.left.isperfect() and self.right.almostCompleteBtrre()
        # if height of left sub tree is equal to height of right sub tree +1
        # then right sub tree must be perfect and left sub tree must be
        # almost complete binary tree
        if heightLeft==height_right+1:
            return self.right.isperfect() and self.left.almostCompleteBtrre()
        return False

        

    def __str__(self):
        return str(self.value)

class Btree:
    def __init__(self):
        self.root = None

    def addRoot(self, item):
        if self.root is None:
            self.root = TreeNode(item)
            return self.root
        else:
            print("Root already exists")
            return self.root

    # convenience wrappers that operate on the root only
    def addLeftChild(self, item):
        if self.root is None:
            print("Root is empty, add a root first")
            return None
        return self.root.addLeftChild(item)

    def addRightChild(self, item):
        if self.root is None:
            print("Root is empty, add a root first")
            return None
        return self.root.addRightChild(item)

    # delete only if the child is a leaf (keeps original behavior)
    def DelLeftChild(self):
        if self.root is None:
            print("Tree is empty")
            return None
        if self.root.left is None:
            print("Left child is not present!")
            return None
        if self.root.left.left is None and self.root.left.right is None:
            x = self.root.left.value
            self.root.left = None
            print(f"Deleted left child with value {x}")
            return x
        print("Left child has its own children, cannot delete directly")
        return None

    def DelRightChild(self):
        if self.root is None:
            print("Tree is empty")
            return None
        if self.root.right is None:
            print("Right child is not present!")
            return None
        if self.root.right.left is None and self.root.right.right is None:
            x = self.root.right.value
            self.root.right = None
            print(f"Deleted right child with value {x}")
            return x
        print("Right child has its own children, cannot delete directly")
        return None


# Example usage
bt = Btree()
root = bt.addRoot(10)
left = bt.addLeftChild(20)
right = bt.addRightChild(30)

# Now these calls work because TreeNode has addLeftChild/addRightChild
left_left = left.addLeftChild(40)
left_right = left.addRightChild(50)
right_left = right.addLeftChild(60)
right_right = right.addRightChild(70)

print("Height:", bt.root.height())        # expected 3
print("Node count:", bt.root.nodeCount()) # expected 7
print("Leaf count:", bt.root.leafCount()) # expected 4

#                 A
#               /   \
#              B     C
#             / \   / \
#            D   E F   G
#              / \
#             H   I
y=Btree()
r=y.addRoot('A')
b=y.addLeftChild('B')
c=y.addRightChild('C')      
d=b.addLeftChild('D')
e=b.addRightChild('E')
f=c.addLeftChild('F')
g=c.addRightChild('G')
h=e.addLeftChild('H')
i=e.addRightChild('I')
print(y.root.almostCompleteBtrre()) #True
print("is perfect:", y.root.isperfect()) #False