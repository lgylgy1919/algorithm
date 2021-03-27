# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def mergeTress(t1, t2):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = self.mergeTress(t1.left, t2.left)
        node.right = self.mergeTress(t1.right, t2.right)

        return node
    else:
        return t1 or t2