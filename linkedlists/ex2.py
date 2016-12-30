from node import Node
from linkedlist import LinkedList

def list_len(head):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    return length

def kth_to_last(head, k):
    current = head
    for i in range(list_len(head) - k - 1): #this way if k > len then it returns first element
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

print kth_to_last(node1, 3).data # should print 4
print kth_to_last(node1, 100).data # should print 1
