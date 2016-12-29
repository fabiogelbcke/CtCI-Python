from node import Node
from linkedlist import LinkedList

def remove_dups(head):
    values = []
    current = head
    prev = None
    while current:
        if current.data in values:
            prev.next = current.next
            current = current.next
        else:
            values.append(current.data)
            prev = current
            current = current.next

node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('1')
node5 = Node('4')
node6 = Node('2')
node7 = Node('5')

ll = LinkedList(node1)
ll.concatenate(node2)
ll.concatenate(node3)
ll.concatenate(node4)
ll.concatenate(node5)
ll.concatenate(node6)
ll.concatenate(node7)

print('before function:')
ll.print_data()

remove_dups(ll.head)
print('after function:')
ll.print_data()
