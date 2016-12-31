class LinkedList:
    def __init__(self, head=None):
        self._head = head
        self._last = head

    @property
    def head(self):
        return self._head

    @property
    def last(self):
        return self._last
    
    def add(self, node):
        node.next = self.head
        self.head = node
        if node.next == None:
            self.last = node

    def concatenate(self, node):
        self.last.next = node
        self.last = node

    def remove(self, data):
        current = self.head
        prev = None
        while current is not None and current.data != data:
            prev = current
            current = current.next
        if current is not None:
            if prev is None: # first one matched data already
                self.head = current.next
            else:
                prev.next = current.next
            if current.next == None:
                self.last = prev

    def print_data(self):
        current = self.head
        while current is not None:
            print current.data
            current = current.next
