class Node:
    def __init__(self, initdata=None):
        self.data = initdata
        self.next = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next_node):
        self.next = next

    def get_next(self):
        return self.next
