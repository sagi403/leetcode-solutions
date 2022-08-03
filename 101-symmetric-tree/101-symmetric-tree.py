# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root:
            return self.checker(root.right, root.left)
        return True
            
    def checker(self, right, left):
        if not right and not left:
            return True
        if not right or not left:
            return False
        if right.val != left.val:
            return False
        return self.checker(right.right, left.left) and self.checker(right.left, left.right)