# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def rearrangeLastN(l, n):
    # Find the last node
    count = 0
    prevNode = None
    node = l
    while node is not None:
        count += 1
        prevNode = node
        node = node.next
    
    if count - n == 0:
        return l
    
    # Connect last node to first
    if prevNode is not None:
        prevNode.next = l
    
    # Find the node to disconnect
    i = 0
    prevNode = None
    while i < count - n:
        i += 1
        prevNode = l
        l = l.next
    
    # Disconnect node
    if prevNode is not None:
        prevNode.next = None
    
    return l
