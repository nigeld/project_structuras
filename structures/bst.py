class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert_recursive(self.root, key)

    def _insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self._insert_recursive(root.right, key)
            else:
                root.left = self._insert_recursive(root.left, key)
        return root
    
    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self._search_recursive(root.right, key)
        return self._search_recursive(root.left, key)

    def inorder_traversal(self):
        self._inorder_recursive(self.root)
        print()

    def _inorder_recursive(self, root):
        if root:
            self._inorder_recursive(root.left)
            print(root.val, end=" ")
            self._inorder_recursive(root.right)


# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia del BST
    bst = BST()

    # Insertar elementos en el BST
    bst.insert([3, "Maria"])
    bst.insert([1, "Daniel"])
    bst.insert([2, "Jose"])
    bst.insert([8, "Maria"])
    bst.insert([0, "Maria"])
    bst.insert([4, "Daniel"])
    bst.insert([5, "Daniel"])

    # Realizar un recorrido en orden (inorder traversal) para imprimir los elementos
    print("Inorder Traversal:")
    bst.inorder_traversal()
