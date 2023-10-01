class Node:
    
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None
        self.level = 0

    def __eq__(self, __value: object) -> bool:
        if __value is None or not isinstance(__value, Node):
            return False
        return self.data == __value.data 
    
    def __repr__(self) -> str:
        return f"Node(data={self.data}, level={self.level})"

    @property
    def isLeaf(self):
        return self.left is None and self.right is None
    
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)
    
    def _insert(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
                return node.right
            else:
                return self._insert(node.right, data)
    
    def print_tree(self, root: Node, level=0, prefix="Root: "):
        if root is not None:
            print(" " * (level * 4) + prefix + str(root.data))
            if root.left is not None or root.right is not None:
                self.print_tree(root.right, level + 1, "    R--- ")
                self.print_tree(root.left, level + 1, "    L--- ")
        else:
            print(" " * (level * 4) + prefix + "None")
    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, node, height):
        if node is None:
            return height
        else:
            left_height = self._height(node.left, height + 1)
            right_height = self._height(node.right, height + 1)
            return max(left_height, right_height)

    def getMin(self, node: Node):
        if node.left is None:
            return node.data
        else:
            return self.getMin(node.left)

    def getMax(self, node: Node):
        if node.right is None:
            return node.data
        else:
            return self.getMax(node.right)
    
    def find(self, data):
        if self.root is not None:
            return self._find(self.root, data)
        else:
            return None
    
    def _find(self, node, data):
        if node is None:
            return None
        elif node.data == data:
            return node
        elif data < node.data:
            return self._find(node.left, data)
        else:
            return self._find(node.right, data)
        
    def delete_node(self, root: Node, data: int):
        if root is None:
            return root
        # Найти узел для удаления
        if data < root.data:
            root.left = self.delete_node(root.left, data)
        elif data > root.data:
            root.right = self.delete_node(root.right, data)
        else:
            # Узел для удаления найден
            # Случай 1: У узла нет потомков или только один потомок
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Случай 2: Узел для удаления имеет два потомка
            temp = self.find_min_value_node(root.right)
            root.data = temp.data
            root.right = self.delete_node(root.right, temp.data)

        return root
                 
    def find_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current
        

tree = BinaryTree()
tree.insert(11)
tree.insert(5)
tree.insert(9)
tree.insert(13)
n = tree.insert(2)
tree.insert(12)
tree.insert(14)
tree.print_tree(tree.root)

tree.delete_node(tree.root, 11)
print("-"*50)
tree.print_tree(tree.root)