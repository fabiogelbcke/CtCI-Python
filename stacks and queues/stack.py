class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None

class Stack:
    def __init__(self, node=None):
        self.top = node
        
    def pop(self):
        if self.top is None:
            return None
        removed_node = self.top
        self.top = self.top.next
        return removed_node.data

    def push(self, node=None):
        if node is not None:
            node.next = self.top
            self.top = node

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

