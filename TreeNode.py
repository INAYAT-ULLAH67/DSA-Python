class TreeNode:
    def __init__(self, value):   # <-- fixed
        self.left = None
        self.value = value
        self.right = None

    def __str__(self):
        return str(self.value)  


