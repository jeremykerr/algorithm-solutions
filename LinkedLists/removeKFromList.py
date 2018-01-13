# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    prev = None
    node = l
    while node is not None:
        remove = False
        if node.value == k:
            remove = True
        if remove and node == l:
            l = node.next
        elif remove:
            prev.next = node.next
        else:
            prev = node
        node = node.next

    return l
    

