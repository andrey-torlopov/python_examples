class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

    def print_tree(self, level=0, prefix="Root: "):
        if self.right:
            self.right.print_tree(level + 1, "R---")
        print(" " * (level * 4) + prefix + str(self.data))
        if self.left:
            self.left.print_tree(level + 1, "L---")
            
    def left_rotation(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        return new_root
    
root = Node(5)
root.left = Node(3)
root.right = Node(8)
root.right.left = Node(7)
root.right.right = Node(10)

if __name__ == '__main__':
    root.print_tree()
    print("-"*50)
    root = root.left_rotation(root)
    root.print_tree()