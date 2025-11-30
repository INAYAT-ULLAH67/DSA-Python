# Python program to check if a 
# given binary tree is perfect

class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

# Function to find depth of tree.
def depth(root):
        d = 0
        node = root
        while node:
            d += 1
            print(d)
            node = node.left
        return d

# Recursive function which checks if 
# tree is perfect or not.
def isPerfectRecur(root, d):
    
    # Empty tree is also perfect 
    if root is None:
        return True
    
    # If node is leaf, check if it 
    # is at depth d.
    if root.left is None and root.right is None:
        return d == 1
    
    # If internal node does not have 
    # left or right node, return false.
    if root.left is None or root.right is None:
        return False
    
    # Check left and right subtree
    return isPerfectRecur(root.left, d-1) \
  	and isPerfectRecur(root.right, d-1)

def isPerfect(root):
    
    # Find depth of tree 
    d = depth(root)
    
    return isPerfectRecur(root, d)

if __name__ == "__main__":
    
    # Binary tree 
    #           10
    #        /     \  
    #      20       30  
    #     /  \     /  \
    #   40    50  60   70
    #        / \
    #      80   90
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)
    # root.left.right.left = Node(80)
    # root.left.right.right = Node(90)

    if isPerfect(root):
        print("True")
    else:
        print("False")