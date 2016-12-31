from node import Node
from linkedlist import LinkedList

def list_len(head):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    return length

def palindrome(head):
    length = list_len(head)
    first_half = []
    current = head
    for i in range(length/2):
        first_half.append(current.data)
        current = current.next
    if length % 2 != 0:
        current = current.next
    first_half.reverse()
    for i in range(length/2):
        if first_half[i] != current.data:
            return False
        current = current.next
    return True

#simple test

node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node4 = Node('5')
node5 = Node('3')
node6 = Node('2')
node7 = Node('1')


ll = LinkedList(node1)
ll.concatenate(node2)
ll.concatenate(node3)
ll.concatenate(node4)
ll.concatenate(node5)
ll.concatenate(node6)
ll.concatenate(node7)


print 'Test 1 - palindrome with odd number of nodes (should be True):'
print 'list:'
ll.print_data()
print 'result:'
print palindrome(ll.head)

ll.remove('5')

print 'Test 2 - palindrome with even number of nodes (should be True):'
print 'list:'
ll.print_data()
print 'result:'
print palindrome(ll.head)

ll.remove('1')

print 'Test 3 - not a palindrome (should be False):'
print 'list:'
ll.print_data()
print 'result:'
print palindrome(ll.head)

print 'Test 4 - single node list with None as data (should be True):'
print 'list:'
single_node = Node()
single_node_list = LinkedList(single_node)
single_node_list.print_data()
print 'result:'
print palindrome(single_node_list.head)

print 'Test 5 - single node list (should be True):'
print 'list:'
single_node.data = '2'
single_node_list.print_data()
print 'result:'
print palindrome(single_node_list.head)
