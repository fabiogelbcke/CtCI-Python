class GraphNode:
    def __init__(self, val=None):
        self.children = []
        self.val = val

    def add_child_directed(self, node):
        if node is not none and node not in self.children:
            self.children.append(node)

class Graph:
    def __init__(self, nodes=[]):
        self.nodes = nodes

    def add_node(self, node):
        if node is not None and node not in self.nodes:
            self.nodes.append(node)
