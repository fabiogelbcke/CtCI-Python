def minimal_tree(nodes):
    if nodes is None or len(nodes) == 0:
        return None
    index = len(nodes)
    node = TreeNode(nodes[index])
    node.left = minimal_tree(nodes[:index])
    node.right = minimal_tree(nodes[index + 1:])
    return node
