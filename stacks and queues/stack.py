class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None

class Stack:
    def __init__(self, node=None):
        self.__top = node
        
    def pop(self):
        if self.__top is None:
            raise IndexError('Pop from empty stack')
        removed_node = self.__top
        self.__top = self.__top.next
        return removed_node.data

    def push(self, node=None):
        if node is not None:
            node.next = self.__top
            self.__top = node

    def peek(self):
        if self.__top is None:
            raise IndexError('Pop from empty stack')
        return self.__top.data

