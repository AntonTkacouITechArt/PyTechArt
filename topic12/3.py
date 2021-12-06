"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head=None, data=set()):
    if head.next is None:
        return False
    else:
        if head in data:
            return True
        else:
            data.add(head)
            a = has_cycle(head.next, data)
            return True if a else False
    
    
