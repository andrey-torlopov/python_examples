class LinkedNode:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def show_list(self) -> None:
        pass
        # print(self.value, self.next)


def createList() -> LinkedNode:
    nodes = list(map(lambda x: LinkedNode(x + 1), list(range(10))))
    head = LinkedNode(0)
    curr = head

    for i in range(len(nodes)):
        curr.next = nodes[i]
        curr = nodes[i]

    return head


def print_linded_list(node) -> None:
    curr = node
    str = ""
    while curr is not None:
        if curr.value is not None:
            str += "%s -> " % curr.value

        curr = curr.next
    str = str[:-3]
    print(str)


def reverse_list(node: LinkedNode) -> LinkedNode | None:
    prev_node = None
    head_next = node

    while head_next is not None:
        next_head = head_next.next
        head_next.next = prev_node
        prev_node = head_next
        head_next = next_head

    return prev_node


node = createList()
print_linded_list(node)
reverse_node = reverse_list(node)
print_linded_list(reverse_node)
