class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None
        self.height = None

class SetOfStacks:
    def __init__(self, capacity=3):
        self.__stacks = []
        self.capacity = capacity

    def peek(self):
        if len(self.__stacks) == 0:
            return None
        return self.__stacks[-1].data

    def push(self, node):
        if len(self.__stacks) == 0 or self.__stacks[-1].height >= self.capacity:
            node.height = 1
            self.__stacks.append(node)
        else:
            node.height = self.__stacks[-1].height + 1
            node.next = self.__stacks[-1]
            self.__stacks[-1] = node

    def pop(self):
        if len(self.__stacks) == 0:
            return None
        removed_data = self.__stacks[-1].data
        if self.__stacks[-1].height == 1:
            self.__stacks.pop()
        else:
            self.__stacks[-1] = self.__stacks[-1].next
        return removed_data
