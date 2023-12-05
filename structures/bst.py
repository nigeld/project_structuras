class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val[0] < key[0]:
                root.right = self._insert_recursive(root.right, key)
            else:
                root.left = self._insert_recursive(root.left, key)
        return root

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.val, end=" ")
            self._inorder_recursive(root.right)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val[0] == key:
            return root
        if root.val[0] < key:
            return self._search_recursive(root.right, key)
        return self._search_recursive(root.left, key)
