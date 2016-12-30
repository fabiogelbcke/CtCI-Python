def delete_middle_node(node):
    next = node.next
    node.data = next.data
    node.next = next.next
