#inorder_traversal_of_a_binary_search_tree

def inorder_traversal(root):
    result = []
    def _inorder(node):
        if node:
            _inorder(node.left)
            result.append(node.val)
            _inorder(node.right)
    _inorder(root)
    return result

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val       # The value of the node
        self.left = left       # Pointer to the left child (or None)
        self.right = right     # Pointer to the right child (or None)


# Example usage:
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left =TreeNode(3)
print(inorder_traversal(root))  # Output: [1, 3, 2]


