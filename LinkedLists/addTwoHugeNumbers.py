# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):

    listA = []
    listB = []
    
    node = a
    while node is not None:
        listA.append(node)
        node = node.next

    node = b
    while node is not None:
        listB.append(node)
        node = node.next
    
    topList = listA
    bottomList = listB
    if len(listA) < len(listB):
        topList = listB
        bottomList = listA
    
    newList = []
    carry = 0
    lastIndex = 0
    for index in range(len(bottomList)):
        lastIndex = index
        rIndex = -(index + 1)
        value = topList[rIndex].value + bottomList[rIndex].value
        if carry:
            value += 1
            carry = 0
        if value > 9999:
            value -= 10000
            carry = 1
        newList.insert(0, ListNode(value))
    
    lastIndex += 1
    while lastIndex < len(topList):
        rIndex = -(lastIndex + 1)
        lastIndex += 1
        value = topList[rIndex].value
        if carry:
            value += 1
            carry = 0
        if value > 9999:
            value -= 10000
            carry = 1
        newList.insert(0, ListNode(value))

    if carry:
        newList.insert(0, ListNode(1))
        
    for index in range(len(newList)):
        if index + 1 < len(newList):
            newList[index].next = newList[index + 1]
            
    return newList[0]