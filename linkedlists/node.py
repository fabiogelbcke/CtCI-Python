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
