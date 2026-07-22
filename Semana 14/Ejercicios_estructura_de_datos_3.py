'''
Ejercicios de Estructuras de Datos 3

Cree una estructura de objetos que asemeje un Binary Tree.
    Debe incluir un método para hacer print de toda la estructura.
    No se permite el uso de tipos de datos compuestos como lists, dicts o tuples ni módulos como collections.
'''

class Node:
    # Represents a single node in a Binary Tree
    def __init__(self, data):
        self.data = data # data: value stored in the node
        self.left = None # Pointer to the left child node
        self.right = None  # Pointer to the right child node

class BinaryTree:
    # Represents the Binary Tree structure
    def __init__(self, root=None):
        # root: starting node of the tree
        self.root = root

    def print_tree(self, node):
        # Preorder traversal: root -> left -> right

        # If node is empty, stop recursion
        if node is None:
            return

        print(node.data)  # Print current node value
        self.print_tree(node.left) # Recursively traverse the left subtree
        self.print_tree(node.right) # Recursively traverse the right subtree

# -------------------------
# Testing the tree
# -------------------------

tree = BinaryTree()

# Root
root = Node("A")
tree.root = root

# Level 1
root.left = Node("B")
root.right = Node("C")

# Level 2 (left side)
root.left.left = Node("D")
root.left.right = Node("E")

# Level 2 (right side)
root.right.left = Node("F")
root.right.right = Node("G")

print("== Tree Traversal ==")
tree.print_tree(tree.root)