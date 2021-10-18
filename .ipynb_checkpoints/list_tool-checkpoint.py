# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
            self.val = x
            self.next = None

def build_list(array):
    linked_list = ListNode(array[0])
    old_node = linked_list
    for i in range(1,len(array)):
        new_node = ListNode(array[i])
        old_node.next = new_node
        old_node = new_node
    return linked_list

def print_list(node):
    while node:
        print(node.val,end=' ')
        node = node.next
    print()