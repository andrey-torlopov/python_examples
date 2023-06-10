class Item(object):
    def __init__(self, next_item=None, prev_item=None, elem=None):
        self.next_item = next_item
        self.prev_item = prev_item
        self.elem = elem


class DoubleLinkedList(object):

    def __init__(self, head=None, tail=None, length=0):
        self.head = head
        self.tail = tail
        self.lenth = length

    def push(self, elem):
        if self.tail is None:
            item = Item(None, None, elem)
            self.head = item
            self.tail = item
            self.length = 1
        else:
            item = Item(None, self.tail, elem)
            self.tail.next_item = item
            self.tail = item
            self.length += 1

    def pop(self):
        try:
            if self.tail is None:
                raise Exception("There is nothing to pop!")
            else:
                self.tail = self.tail.prev_item
                if self.tail is not None:
                    self.tail.next_item = None
                self.length -= 1
        except Exception as error:
            print("Caugth this error: " + error.args[0])

    def unshift(self, elem):
        ''' Добавляет элемент в начало списка'''
        if self.head is None:
            item = Item(None, None, elem)
            self.head = item
            self.tail = self.head
            self.length = 1
        else:
            item = Item(self.head, None, elem)
            self.head.prev_item = item
            self.head = self.head.prev_item
            self.length += 1

    def shift(self, elem):
        '''Убирет элемент из начала списка'''
        try:
            if self.head is None:  # length == 0
                raise Exception('There is nothing to shift!')
            else:
                self.head = self.head.next_item
                if self.head is not None:
                    self.head.prev_item = None
                self.length -= 1
        except Exception as error:
            print("Caught this error: " + error.args[0])

    def len(self):
        ''' Длина списка'''
        return self.length

    def delete(self, elem):
        ''' Удаляем элемент из списка'''
        if self.head is None:
            pass
        elif self.head.elem == elem:
            self.shift()
        else:
            cur = self.head.next_item
            while cur is not None:
                if (cur.elem == elem) and (cur.next_item is not None):
                    temporary_item = cur.prev_item.next_item
                    cur.prev_item.next_item = cur.next_item.prev_item
                    cur.next_item.prev_item = temporary_item
                    self.length -= 1
                    break
                elif (cur.elem == elem) and (cur.next_item is None):
                    cur.prev_item.next_item = None
                    self.tail = cur.prev_item
                    self.length -= 1
                    break
                else:
                    cur = cur.next_item
