from node import Node
from linkedlist import LinkedList

def loop_detection(head):
    current = head
    ids_list = []
    while current is not None:
        if id(current) in ids_list:
            return current
        ids_list.append(id(current))
        current = current.next
    return False

node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('4')
node5 = Node('5')
node6 = Node('6')
node7 = Node('7')

ll = LinkedList(node1)
ll.concatenate(node2)
ll.concatenate(node3)
ll.concatenate(node4)
ll.concatenate(node5)
ll.concatenate(node6)
ll.concatenate(node7)

print 'Test 1 - list is not circular. Should return False'
print loop_detection(node1)

node7.next = node3

print 'Test2 - list is circular. Should print the id of the first node on circle, which is {}'.format(id(node3))
print id(loop_detection(node1))
