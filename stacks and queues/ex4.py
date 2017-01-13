from stack import Node, Stack


class MyQueue:
    def __init__(self, node=None):
        self.temp_stack = Stack()
        self.main_stack = Stack(node)

    def is_empty(self):
        return True if self.main_stack.top is None else False

    def add(self):
        
