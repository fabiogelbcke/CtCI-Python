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
    """
    Implementation of a triple stack using only one list.
    I'm storing the elements of the 1st stack on indexes with
    i % 3 == 0, 2nd stack on indexes with i % 3 == 1, and
    3rd stack on indexes with i % 3 == 2.
    Since indexes on python lists are sequential (i.e. you can't 
    have a list with 10 elements and then add something at position 15),
    everytime I add a new element that's beyond the current length of
    the list, I add None to fields as necessary. E.g. if the list has
    length 15 and there are already 5 elements on stack 2
    (indexes 1,4,7,10,13), if I need to add something to stack 2, it goes
    on index 16. I add None on index 15, the node on index 16 and None on index
    17. If I need to do it again, i add None on index 18, the node on 19 and
    None on 20, and so on
    """

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
