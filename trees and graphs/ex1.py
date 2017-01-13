from graph import GraphNode, Graph

def route_exists(node1, node2, visited=[]):
    if node1 is None or node2 is None:
        return False
    curr = node1
    if node1 == node2:
        return True
    for child in node1.children:
        if id(child) not in visited:
            visited.append(id(child))
            if route_exists(child, node2, visited) is True:
                return True
    return False

g = Graph()
for i in range(10):
    g.add_node(GraphNode(i))
g.nodes[0].children += [g.nodes[2], g.nodes[4], g.nodes[6]]
g.nodes[2].children += [g.nodes[3]]
g.nodes[3].children += [g.nodes[2], g.nodes[4]]
g.nodes[4].children += [g.nodes[3], g.nodes[0]]
g.nodes[5].children += [g.nodes[7]]
g.nodes[6].children += [g.nodes[0], g.nodes[7]]
g.nodes[7].children += [g.nodes[6], g.nodes[5], g.nodes[8]]
g.nodes[8].children += [g.nodes[7], g.nodes[9]]
g.nodes[9].children += [g.nodes[9]]

print route_exists(g.nodes[0], g.nodes[9])
