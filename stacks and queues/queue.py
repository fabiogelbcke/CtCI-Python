class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None

class Queue:
    def __init__(self, node=None):
        self.__front = node
        self.last = node
        
    def remove(self):
        if self.__front is None:
            raise IndexError('Remove from empty queue')
        removed_node = self.__front
        self.__front = self.__front.next
        if self.__front == None:
            self.last = None
        return removed_node.data

    def add(self, node=None):
        if node is not None:
            if self.last is not None:
                self.last.next = node
            else:
                self.__front = node
                self.last = node
            self.last = node

    def peek(self):
        if self.__front is None:
            raise IndexError('Remove from empty queue')
        return self.__front.data

    def is_empty(self):
        if self.__front is None:
            return True
        return False
