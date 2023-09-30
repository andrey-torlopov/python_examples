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

    def tree_to_array(self) -> [int]:
        array = []
        if self.left:
            array += self.left.tree_to_array()
        array.append(self.data)
        if self.right:
            array += self.right.tree_to_array()
        return array
        
array = [8, 3,0, 10, 6, 14,4,7,13,2]
root = Node(array[0])
array = array[1:]

for item in array:
    current = root
    while True:
        if item > current.data:
            if current.right is None:
                current.right = Node(item)
                break
            else:
                current = current.right
        else:
            if current.left is None:
                current.left = Node(item)
                break
            else:
                current = current.left

root.print_tree()
a1 = root.tree_to_array()
print(array, a1)