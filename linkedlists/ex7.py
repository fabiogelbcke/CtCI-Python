from node import Node
from linkedlist import LinkedList

def get_ids(head):
    ids_list = []
    current = head
    while current is not None:
        ids_list.append(id(current))
        current = current.next
    return ids_list
        
def intersection(head1, head2):
    ids_list1 = get_ids(head1)
    ids_list2 = get_ids(head2)
    match_index = None
    for i in range(len(ids_list1)):
        if ids_list1[i] in ids_list2:
            match_index = i
            break
    if match_index is None:
        return False
    current = head1
    for i in range(match_index):
        current = current.next
    return current


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

node8 = Node('4')
node9 = Node('5')
node10 = Node('6')


ll2 = LinkedList(node8)
ll2.concatenate(node9)
ll2.concatenate(node10)

print 'Test 1 - non intersecting lists. Should print False'
print intersection(node1, node8)

ll2.concatenate(node3)

print 'Test 2 - intersecting lists'
print 'Should print {} which is the id of the intersecting node'.format(str(id(node3)))

print id(intersection(node1, node8))
