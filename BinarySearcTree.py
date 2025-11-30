from TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        # Base case: empty spot found
        if root is None:
            return TreeNode(value)

        # if a value is less than root, go left; else go right
        if value < root.value:
            # insert in the left subtree and update left child pointer 
            # when we found the place in the node that is None we insert the new node there
            root.left = self.insert(root.left, value)
        elif value > root.value:
            root.right = self.insert(root.right, value)
        # Equal keys are not inserted in BST
        return root

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)
    def search(self, node, target):
        #if
        if node is None:
            return None
        elif node.value == target:
            return node
        elif target < node.value:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)
    def  minValueNode(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
    def deletionOfNode(self,node,value):
        if not node:
            return None
        #if value is less than node's value, go left
        if value < node.value:
            node.left = self.deletionOfNode(node.left,value)
        #if value is greater than node's value, go right
        elif value > node.value:
            node.right = self.deletionOfNode(node.right,value)
        else:
            #with no children 
            if node.left is None and node.right is None:
                return None
            #with one child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            #with two children
            temp = self.minValueNode(node.right)
            node.value = temp.value
            node.right = self.deletionOfNode(node.right,temp.value)
        return node     
    
A=BinarySearchTree()
A.root = A.insert(A.root, 50)
A.insert(A.root, 30)
A.insert(A.root, 20)
A.insert(A.root, 40)
A.insert(A.root, 70)
A.insert(A.root, 60)
A.insert(A.root, 80)
print("Inorder traversal of the BST:")
A.inorder(A.root)
print()
result = A.search(A.root, 60)
if result:
    print(f"Value {result.value} found in the BST.")
else:
    print("Value not found in the BST.")
result = A.search(A.root, 25)
if result:
    print(f"Value {result.value} found in the BST.")
else:
    print("Value not found in the BST.")
B = BinarySearchTree()
B.root = B.insert(B.root, 13)
B.insert(B.root, 7)
B.insert(B.root, 3)
B.insert(B.root, 8)
B.insert(B.root, 15)
B.insert(B.root, 14)
B.insert(B.root, 19)
B.insert(B.root, 18)

print("Inorder traversal of BST B:")
B.inorder(B.root)
print()
print("Delete 8:")
B.root = B.deletionOfNode(B.root,8)
B.inorder(B.root)

print()
print("Delete 15:")
B.root = B.deletionOfNode(B.root,15)
B.inorder(B.root)       

