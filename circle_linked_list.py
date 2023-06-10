class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class CircularLinkedList:
    
    # Empty list
    def __init__(self) -> None:
        self.head = None
        
    
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head
        ptr1.next = self.head
        
        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = ptr1
        else:
            ptr1.next = ptr1
        
        self.head = ptr1
        
        
    def printList(self):
        temp = self.head
        if self.head is not None:
            while(True):                
                print(temp.data)
                temp = temp.head
                if (temp == self.head):
                    break
                



a = CircularLinkedList()
a.push(1)
a.push(2)
a.push(3)

a.printList()

