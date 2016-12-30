from node import Node
from linkedlist import LinkedList

def get_number(head):
    current = head
    num_list = []
    while current is not None:
        num_list.append(str(current.data))
        current = current.next
    num_list.reverse()
    num = int(''.join(num_list))
    return num

def num_to_list(num):
    temp_list = str(num)
    temp_list = list(temp_list)
    temp_list.reverse()
    current = Node(int(temp_list[0]))
    head = current
    prev = None
    for i in range(1, len(temp_list)):
        prev = current
        current = Node(int(temp_list[i]))
        prev.next = current
    return head

def sum_lists(head1, head2):
    num1 = get_number(head1)
    num2 = get_number(head2)
    num_sum = num1 + num2
    return num_to_list(num_sum)

node1 = Node('1')
node2 = Node('2')
node3 = Node('3')

node4 = Node('1')
node5 = Node('4')
node6 = Node('2')
node7 = Node('5')

ll1 = LinkedList(node1)
ll1.concatenate(node2)
ll1.concatenate(node3)

ll2 = LinkedList(node4)
ll2.concatenate(node5)
ll2.concatenate(node6)
ll2.concatenate(node7)

result = sum_lists(node1, node4)

result_list = LinkedList(result)
result_list.print_data()
