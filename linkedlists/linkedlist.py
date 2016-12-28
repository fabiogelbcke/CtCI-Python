class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.last = head

    def add(self, node):
        node.set_next(self.head)
        self.head = node
        if node.next == None:
            self.last = node

    def remove(self, data):
        current = self.head
        prev = None
        while current is not None and current.get_data() != data:
            prev = current
            current = current.get_next()
        if current is not None:
            if prev is None: # first one matched data already
                self.head = current.get_next()
            else:
                prev.set_next(current.get_next())
            if current.get_next() == None:
                self.last = prev
        
