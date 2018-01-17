#
# Definition for binary tree:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def hasPathWithGivenSum(t, s):
    tLeft = False
    tRight = False
    if t is None:
        if s is 0:
            return True
        return False
    if t.left is not None:
        tLeft = hasPathWithGivenSum(t.left, s-t.value)
    if t.right is not None:
        tRight = hasPathWithGivenSum(t.right, s-t.value)
    if t.left is None and t.right is None:
        return s == t.value
    return tLeft or tRight

