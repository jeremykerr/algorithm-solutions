# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def value(node):
    if node is None:
        return node
    return node.value

def valueNext(node):
    if node is None:
        return None
    elif node.next is None:
        return None
    return node.next.value

def reverseNodesInKGroups(l, k):

    # -----------------------------------
    # If at least k nodes exist, continue
    # -----------------------------------
    sL = l
    for i in range(k):
        if sL is None:
            return l
        sL = sL.next
    
    # ----------------
    # Memory footprint
    # ----------------
    # -> p: prior
    # -> c: current
    # -> n: next
    p = None
    c = l
    n = c.next
    
    #print("L: %s" % value(l))
    for i in range(k):
        #print("\ti: %s" % i)
        
        # ------------
        # Flip pointer
        # ------------
        n = c.next
        c.next = p
        #print("\t\t(%s) -> (%s)" % (value(c), valueNext(c)))
        #print("\t\tP: %s; C: %s; N: %s" % (value(p), value(c), value(n)))
        
        # ------------
        # Step forward
        # ------------
        p = c
        c = n
        if n is not None:
            n = n.next
    
    #print("C: %s" % (value(c)))
    c = reverseNodesInKGroups(c, k)

    l.next = c
    l = p
    
    # -------------
    # Return result
    # -------------
    return l
