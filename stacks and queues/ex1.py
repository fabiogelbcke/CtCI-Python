class Node:
    def __init__(self, initdata=None):
        self._data = initdata
        self._next = None

    @property
    def data(self):
        return self._data

    @property
    def next(self):
        return self._next

class TripleStack:
    def __init__(self):
        self._triplestack = []

    @property
    def triplestack(self):
        return self._triplestack

    def generic_push(self, node, stack_no):
        i = 0
        while 3*i < len(self.triplestack) and self.triplestack[3*i + stack_no] is not None:
            i += 1
        if 3*i >= len(self.triplestack):
            self.triplestack += [None,None,None]
        self.triplestack[3*i + stack_no] = node

    def push_stack1(self, node=None):
        self.generic_push(node, 0)

    def push_stack2(self, node=None):
        self.generic_push(node, 1)

    def push_stack3(self, node=None):
        self.generic_push(node, 2)

    def generic_pop(self, stack_no):
        last_index = len(self.triplestack) - (3 - stack_no)
        while last_index > 0 and self.triplestack[last_index] is None:
            last_index -= 3
        if last_index >= 0:
            removed_node = self.triplestack[last_index]
            self.triplestack[last_index] = None
            return removed_node.data
        return None

    def pop_stack1(self):
        return self.generic_pop(0)

    def pop_stack2(self):
        return self.generic_pop(1)

    def pop_stack3(self):
        return self.generic_pop(2)

    def generic_peek(self, stack_no):
        last_index = len(self.triplestack) - (3 - stack_no)
        while last_index > 0 and self.triplestack[last_index] is None:
            last_index -= 3
        if last_index >= 0:
            return self.triplestack[last_index].data
        return None

    def peek_stack1(self):
        return self.generic_peek(0)

    def peek_stack2(self):
        return self.generic_peek(1)

    def peek_stack3(self):
        return self.generic_peek(2)
