#implementation of binary search tree
#creating class treenode
class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
#creating a bst class
class BST:
    def __init__(self):
        self.root = None
        
#inserting a value
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)
        #helper function for insert
    def _insert(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)


# searching a value
    def search(self, key):
        return self._search(self.root, key)
        #helper function for searching
    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
#deleting a value
    def delete(self, key):
        self.root = self._delete(self.root, key)
        #helper function for deleting 
    def _delete(self, node, key):
        if not node:
            return node
        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            #case1
            if not node.left:
                return node.right
            #case2
            if not node.right:
                return node.left
            #case3
            temp_val = self._min_value_node(node.right).val
            node.val = temp_val
            node.right = self._delete(node.right, temp_val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

# Example usage:
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

print(bst.search(30).val)  # Output: 30
bst.delete(20)
print(bst.search(20))  # Output: None