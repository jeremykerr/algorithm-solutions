# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def isListPalindrome(l):
    forwardL = []
    node = l
    while node is not None:
        forwardL.append(node.value)
        node = node.next

    for x, y in zip(forwardL, reversed(forwardL)):
        if x != y:
            return False

    return True
